from pydantic import BaseModel

class VMOutput(BaseModel):
    stdin: str = ""
    stdout: str = ""
    stderr: str = ""
    returncode: int = -1
    runtime: str = ""