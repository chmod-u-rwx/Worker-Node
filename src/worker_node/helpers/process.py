import subprocess

def clean_process(proc: subprocess.Popen[str], timeout: int =5):
    if proc.poll() is None:
        proc.terminate()

        try:
            proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait()
