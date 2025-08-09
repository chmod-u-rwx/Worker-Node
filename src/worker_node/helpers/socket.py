import time
import socket

def wait_for_file_socket_availability(file_socket: str, timeout: int=10):
    start = time.time()

    while time.time() - start < timeout:
        try:
            with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
                sock.connect(file_socket)
                return True
        except (FileNotFoundError, ConnectionRefusedError):
            time.sleep(0.5)

    return False

