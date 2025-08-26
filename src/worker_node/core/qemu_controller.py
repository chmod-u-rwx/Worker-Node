import os
import shutil
import time
import subprocess
import socket
import random
import requests
from pathlib import Path
from enum import Enum
from typing import Any, List, Optional 

from ..helpers.process import clean_process
from ..models.qemu_load import QemuLoad
from ..helpers.process import clean_process
from ..helpers.socket import wait_for_tcp_monitor, get_free_port
from ..config import BASE_IMG_FILE, VIRTUALIZATION, LOCAL_JOB_REPOSITORY_CACHE_PATH
from ..models.vm_output import VMOutput
import paramiko

class QemuStatus(Enum):
    STARTED = 1
    STOPPED = 2
    RUNNING = 3

class QemuController:
    def __init__(self, img_path: Path, cpu_count: int = 1, memory_allocated: int = 0, ) -> None:
        if not os.path.exists(BASE_IMG_FILE):
            raise FileNotFoundError("Base img does not exist")
        
        self.img_path = img_path 
        self.cpu_count = cpu_count
        self.snapshot_name = "basetest"
        self.memory_allocated = memory_allocated
        self.status = QemuStatus.STOPPED
        self.boot_time = 0
        self.ssh = paramiko.SSHClient()
        self.monitor_tcp_port = get_free_port()

        # Copy the base img file into img_path
        shutil.copy(BASE_IMG_FILE, img_path)
        self.create_snapshot()

    def start(self):
        if self.img_path.exists() == False:
            raise RuntimeError(f"QEMU img not found at {self.img_path}. Ensure that PATH to img is correct.")

        if self.status == QemuStatus.STARTED:
            raise RuntimeError("QEMU is already running")        
        
        command = self._get_qemu_cmd(True)

        try:
            start_time = time.perf_counter()
            
            self.proc = subprocess.Popen(command, text=True)
            time.sleep(0.5)
            if self.proc.poll() is not None:
                raise RuntimeError(f"Failed to start QEMU process due to an error in the command. Return Code {self.proc.returncode}")
            
            if (self.wait_for_ssh_connection()):
                self.boot_time = (time.perf_counter() - start_time)*1000

            self.status = QemuStatus.STARTED
            self._mount_local_job_repo_cache()
            print(f"VM booted in {self.boot_time:.2f} ms.")

        except FileNotFoundError:
            self.status = QemuStatus.STOPPED
            raise RuntimeError("QEMU img not found. Ensure that PATH to img is correct.")
        except Exception as e:
            self.status = QemuStatus.STOPPED
            raise RuntimeError(f"An unexpected error occurred: {str(e)}")
    
    def stop(self):
        if self.status != QemuStatus.STARTED:
            raise RuntimeError("QEMU is not STARTED")

        if self.proc:
            clean_process(self.proc)

            self.status = QemuStatus.STOPPED
            print("VM stopped successfully.")
        else:
            raise RuntimeError("No QEMU process found")

    def reset(self) -> None:
        if self.status != QemuStatus.STARTED:
            raise Exception("Qemu has not yet started")
        
        try:
            self.freeze()
            self._send_command_to_qemu_monitor(f"loadvm {self.snapshot_name}")
            self.resume()
        except Exception as e:
            raise RuntimeError(f"Failed to reset vm. An unexpected error occured: {e}")

    def freeze(self):
        if self.status != QemuStatus.STARTED:
            raise Exception("Qemu has not yet started")

        try:
            self._send_command_to_qemu_monitor("stop")
        except (RuntimeError, TimeoutError) as e:
            raise RuntimeError("Failed to freeze vm") from e
        
    def resume(self):
        if self.status != QemuStatus.STARTED:
            raise Exception("Qemu has not yet started")

        try:
            self._send_command_to_qemu_monitor("cont")
        except (RuntimeError, TimeoutError) as e:
            raise RuntimeError("Failed to resume vm") from e
        
    def run_command(self, command:List[str], timeout:int = 30) -> VMOutput:
        start_time = time.perf_counter()
        if self.status != QemuStatus.STARTED:
            raise RuntimeError("QEMU is not STARTED. Cannot run command.")
        
        if not (self.ssh.get_transport() and self.ssh.get_transport().is_active()): # type:ignore
            self.wait_for_ssh_connection()
        
        self.status = QemuStatus.RUNNING
        cmd = " ".join(command)
        error_buffer = ""

        while (time.perf_counter() - start_time) < timeout:
            try:
                _, stdout, stderr = self.ssh.exec_command(cmd)
                returncode = stdout.channel.recv_exit_status()

                output = VMOutput(
                    stdin=cmd,
                    stdout=stdout.read().decode("utf-8"),
                    stderr=stderr.read().decode("utf-8"),
                    returncode=returncode,
                    runtime=f"{(time.perf_counter() - start_time) * 1000:.2f} ms"
                )        
                return output

            except RuntimeError as e:
                error_buffer = f"Runtime error: {str(e)}\n"
                time.sleep(1)
            except paramiko.SSHException as e:
                error_buffer = f"SSH error: {str(e)}\n"
                time.sleep(1)
            except Exception as e:
                error_buffer = f"Unexpected error: {str(e)}\n"
                time.sleep(1)
            finally:
                self.status = QemuStatus.STARTED

        raise TimeoutError(f"Command execution timed out after {timeout} seconds. Last known error: {error_buffer}")

    def create_snapshot(self):
        proc_qemu = self._start_qemu_no_loadvm()
        vm_ip = self._listen_for_vm_ip()
        if not vm_ip:
            raise RuntimeError("Failed to get vm ip")
        self.vm_ip = vm_ip.split(":")[1] 

        try:
            self._wait_qemu_monitor_socket(proc_qemu)
            self.wait_for_ssh_connection()
            self._send_command_to_qemu_monitor(f"savevm {self.snapshot_name}")
        finally:
            clean_process(proc=proc_qemu)

    def send_http_request_to_vm(self, method: str,
                                path: str,
                                port: int,
                                query_params: Optional[dict[str, Any]] = None,
                                body: Optional[dict[str, Any]] = None,  
                                headers: Optional[dict[str, str]] = None, 
                                ) -> Any:

        if not self.status != QemuStatus.RUNNING:
            raise RuntimeError("Qemu has not yet started.") 

        url = f"http://{self.vm_ip}:{port}{path}"

        try:
            response = requests.request(
                method=method,
                url=url,
                params=query_params,
                json=body,
                headers=headers
                )

            # if response is an http error, raise it
            response.raise_for_status()

            # useful if server doesnt return json response
            try:
                return response.json()
            except ValueError:
                return response.text
            
        except requests.RequestException as e:
            return {
                "error": str(e),
                "type": type(e).__name__,
                "url": getattr(e.request, "url", None),
                "status_code": getattr(getattr(e, "response", None), "status_code", None)
            }

    def get_resource_load(self) -> QemuLoad:
        if self.status != QemuStatus.STARTED:
            raise Exception("Qemu has not yet started")

        try:
            result = subprocess.run(["ps", "-p", str(self.proc.pid), "-o", "pcpu=,rss=,pid="],
                                    capture_output=True,
                                    text=True,
                                    check=True)
        except FileNotFoundError:
            raise RuntimeError("ps command not found. Not installed?")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"ps failed: {e.stderr.strip()}")

        cpu_usage, memory_usage, pid = result.stdout.strip().split(" ")
        return QemuLoad(
            # %cpu returns the usage summed across all cores, so we have to divide it
            # by the cpu_count normalizes it relative to the allocated cpu_count
            cpu_usage= float(cpu_usage) / self.cpu_count,      # in percentage
            memory_usage= float(memory_usage) // 1024.0,       # this is in MB
            pid= int(pid)
        )    

    def _get_qemu_cmd(self, loadvm: bool = False) -> list[str]:
        """
        Returns the proper qemu command based on virtualization.
        Loads self.snapshot if loadvm = True
        """
        
        accel = "tcg" if VIRTUALIZATION == "darwin" else "kvm:tcg,usb=off"
        cpu = "max" if VIRTUALIZATION == "darwin" else "host"
        netdev = "vmnet-bridged,ifname=en0,id=net0" if VIRTUALIZATION == "darwin" else "bridge,id=net0,br=br0"
        mac_address = self._generate_mac_address()

        # Enables TCP qemu monitor
        monitor_chardev = f"socket,id=mon1,host=127.0.0.1,port={self.monitor_tcp_port},server=on,wait=off"
        monitor = "chardev=mon1,mode=readline"

        cmd = [
            "qemu-system-x86_64",
            "-machine", f"accel={accel}",
            "-cpu", cpu,
            "-smp", str(self.cpu_count),
            "-m", f"{self.memory_allocated}M",
            "-hda", str(self.img_path),
            "-netdev", netdev,
            "-device", f"virtio-net,netdev=net0,mac={mac_address}",
            "-chardev", monitor_chardev,
            "-mon", monitor,
            "-serial", "mon:stdio", 
            "-fsdev", f"local,id=fsdev0,path={LOCAL_JOB_REPOSITORY_CACHE_PATH},security_model=none",
            "-device", "virtio-9p-pci,fsdev=fsdev0,mount_tag=jobcache",
            "-nographic"
        ]

        if VIRTUALIZATION == "linux":
            cmd.append("-enable-kvm")
        else:
            cmd.insert(0, "sudo") # sudo is required for macos

        if loadvm:
            cmd.extend(["-loadvm", self.snapshot_name])

        return cmd 
    
    def _generate_mac_address(self) -> str:
        """
        This is used to assign to qemu instance (in a flag) to ensure each vm instance
        gets a unique ip address.
        """
        
        # First byte: 0x02 = unicast + locally administered
        mac = [0x02] + [random.randint(0x00, 0xFF) for _ in range(5)]
        return ":".join(f"{b:02x}" for b in mac)

    def _start_qemu_no_loadvm(self) -> subprocess.Popen[str]:
        qemu_cmd = self._get_qemu_cmd()

        try:
            proc_qemu = subprocess.Popen(
                qemu_cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
                text=True)
            
            return proc_qemu
            
        except FileNotFoundError:
            raise RuntimeError("Qemu binary not found. Not installed?")

    def _wait_qemu_monitor_socket(self, proc_qemu: subprocess.Popen[str], host: str = "127.0.0.1", timeout: int = 10):
        if wait_for_tcp_monitor(host=host, port=self.monitor_tcp_port, timeout=timeout):
            return
        
        # Read stderr if we failed to wait for tcp monitor
        try:
            _, qemu_stderr = proc_qemu.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            qemu_stderr = "Timeout reading QEMU stderr"
        finally:
            clean_process(proc_qemu)

        raise RuntimeError(f"QEMU TCP monitor failed to start in time.\nQEMU stderr: {qemu_stderr}")

    def _send_command_to_qemu_monitor(self, command: str, host: str='127.0.0.1', timeout: float = 2.0) -> str:
        """
        Sends a command to the QEMU monitor via TCP and returns the full output.
        Raises RuntimeError on connection issues or decoding errors.
        """
        output = b""
        try:
            with socket.create_connection((host, self.monitor_tcp_port), timeout=timeout) as sock:
                sock.sendall(f"{command}\n".encode())
                sock.settimeout(timeout)
                
                while True:
                    try:
                        chunk = sock.recv(4096)
                        if not chunk:
                            break
                        output += chunk
                    except socket.timeout:
                        break
        except Exception as e:
            raise RuntimeError(f"Failed to connect or communicate with QEMU monitor at {host}:{self.monitor_tcp_port}: {e}") from e

        try:
            return output.decode().strip()
        except UnicodeDecodeError as e:
            raise RuntimeError(f"Failed to decode QEMU monitor response: {e}") from e

    def wait_for_ssh_connection(self, user:str="root",password:str="root", timeout:int=60) -> None:
        """
        Poll SSH on localhost:port until authentication succeeds,
        meaning the server is ready for communication.
        """
        # if self.status != QemuStatus.STARTED:
        #     raise RuntimeError("QEMU is not STARTED. Cannot wait for SSH connection.")

        start_time = time.perf_counter()
        while (time.perf_counter() - start_time) < timeout:
            try:
                self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                self.ssh.connect(self.vm_ip, username=user, password=password, timeout=1)
                return
            except Exception:
                time.sleep(0.05)

        raise TimeoutError("SSH authentication failed. Server not ready.")
    
    def _mount_local_job_repo_cache(self):
        try:
            self.run_command(command=["mkdir -p /mnt/jobcache"]) # this is where we mount
            self.run_command(command=["mount -t 9p -o trans=virtio jobcache /mnt/jobcache"])
        except Exception as e:
            raise RuntimeError(f"Failed to mount local job repository cache path in /mnt/jobcache: {e}")

    def _listen_for_vm_ip(self, timeout: int=120) -> str:
        PORT = 9999
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.bind(("", PORT))

            start_time = time.perf_counter()
            while (time.perf_counter() - start_time) < timeout:
                data, _ = sock.recvfrom(1024)
                try:
                    msg = data.decode("utf-8").strip()
                    return msg
                except UnicodeDecodeError:
                    continue
        # socket auto-closed here
        return ""

    def delete(self):
        ...

