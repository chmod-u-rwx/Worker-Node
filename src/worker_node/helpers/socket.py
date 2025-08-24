import time
import socket

def wait_for_tcp_monitor(port: int, host: str='127.0.0.1', timeout:int=10) -> bool:
    """Wait until the QEMU TCP monitor is available."""
    start = time.time()
    while time.time() - start < timeout:
        try:
            with socket.create_connection((host, port), timeout=1):
                return True
        except (ConnectionRefusedError, OSError):
            time.sleep(0.2)
    return False

def get_free_port() -> int:
    """Lets OS pick a free port for qemu-monitor tcp socket use"""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 0))
        assigned_port = s.getsockname()[1]
    return assigned_port