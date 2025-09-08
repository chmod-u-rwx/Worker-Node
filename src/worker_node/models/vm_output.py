from pydantic import BaseModel
from typing import Any

class VMOutput(BaseModel):
    stdin: str = ""
    stdout: Any = ""
    stderr: str = ""
    returncode: int = -1
    runtime: str = ""