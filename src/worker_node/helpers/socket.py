import time
import socket

def wait_for_tcp_monitor(host: str='127.0.0.1', port: int=5555, timeout:int=10) -> bool:
    """Wait until the QEMU TCP monitor is available."""
    start = time.time()
    while time.time() - start < timeout:
        try:
            with socket.create_connection((host, port), timeout=1):
                return True
        except (ConnectionRefusedError, OSError):
            time.sleep(0.2)
    return False

