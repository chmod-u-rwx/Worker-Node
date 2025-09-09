from pydantic import BaseModel

class QemuLoad(BaseModel):
	cpu_usage: float
	memory_usage: float
	pid: int