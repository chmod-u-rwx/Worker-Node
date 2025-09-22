import os
import subprocess
import pyuac #type:ignore

def enable_tap(name:str="TAP0", old_adapter_name:str="TAP-Windows Adapter V9"):
    try:
        check_TAP0 = subprocess.run(
            ["netsh", "interface", "set", "interface", f"name={name}"],
            capture_output=True,
            text=True,
            shell=True
        )
        
        if check_TAP0.returncode != 0:
            _rename_tap(new_name=name, old_name=old_adapter_name)

        subprocess.run(
        ["netsh", "interface", "set", "interface", f"name={name}", "admin=enabled"],
        capture_output=True,
        text=True,
        shell=True
        )
        
        result_check_admin = subprocess.Popen(["netsh", "interface", "show", "interface", f"name={name}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        stdout, stderr = result_check_admin.communicate() #type: ignore

        for line in stdout.splitlines(): #type: ignore
            if "Administrative state" in line:
                admin_state = line.split(":")[1].strip()# type: ignore
                if admin_state.lower() == "enabled":
                    _enable_ics()
                elif admin_state.lower() == "disabled":
                    raise RuntimeError(f"{name} is disabled. Please enable TAP Administrative State manually.")

    except subprocess.CalledProcessError:
        raise RuntimeError(f"Failed to rename or enable TAP adapter")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")

def _rename_tap(new_name:str="TAP0", old_name:str="TAP-Windows Adapter V9"):
    subprocess.run(
        ["netsh", "interface", "set", "interface", old_name, "newname=" + new_name],
        check=True, shell=True
    )

def _enable_ics():
    path = os.path.abspath("enable_tap_ics.ps1")
    try:
        subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", path], check=True)
    except subprocess.CalledProcessError:
        raise RuntimeError("It either worked or failed, run qemu if network bridge connected")
    except Exception as e:
        raise RuntimeError(f"Unexpected error occurred while enabling ICS: {e}")
    
if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin() # type:ignore
    enable_tap()