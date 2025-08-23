from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional
from enum import Enum

class NodeStatus(Enum):
    ACTIVE = "started"
    INACTIVE = "stopped"

class Node(BaseModel):
    node_id: UUID = Field(..., description="Id for node")
    status: NodeStatus = Field(...)

    job_slots: int = Field(..., ge=0, description="Available job slots. This are scaled base on number of jobslots")

    cpu_percentage_allocated: float = Field(..., ge=0, description="Number of CPUs allocated")
    cpu_count_allocated: int = Field(..., ge=1, description="Number of CPUs allocated")
    memory_allocated: int = Field(..., ge=1, description="Memory allocated in MB")
    cache_size_allocated: int = Field(..., ge=1, description="Size of cache")

    cpu_usage: float = Field(default=0, ge=0, description="Cpu percentage used")
    memory_usage: int = Field(default=0, ge=0, description="Memory allocated in MB")
    cache_size_usage: int = Field(default=0, ge=1, description="Size of cache")

class NodeUpdates(BaseModel):
    job_slots: Optional[int] = Field(default=None, ge=0, description="Available job slots. This are scaled base on number of jobslots")

    cpu_percentage_allocated: Optional[float] = Field(default=None, ge=0, description="Number of CPUs allocated")
    cpu_count_allocated: Optional[int] = Field(default=None, ge=1, description="Number of CPUs allocated")
    memory_allocated: Optional[int] = Field(default=None, ge=1, description="Memory allocated in MB")
    cache_size_allocated: Optional[int] = Field(default=None, ge=1, description="Size of cache")

    cpu_usage: Optional[float] = Field(default=None, ge=0, description="Cpu percentage used")
    memory_usage: Optional[int] = Field(default=None, ge=0, description="Memory allocated in MB")
    cache_size_usage: Optional[int] = Field(default=None, ge=1, description="Size of cache")


