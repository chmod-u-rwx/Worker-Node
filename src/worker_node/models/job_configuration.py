from enum import Enum
from typing import Annotated, Any, Optional
from typing import Union
from pydantic import BaseModel, Field

from .io_types import HttpInput, BinaryInput, FileInput, Output, Error

class SupportedRuntimes(Enum):
    PYTHON = "python"
    NODE = "node"
    DOTNET = "dotnet"


class ProjectDetails(BaseModel):
    name: str = Field(...)  
    description: str = Field(...)  
    version: str = Field(...)  
    owner: str = Field(...)  

class RunDetails(BaseModel):
    runtime: SupportedRuntimes = Field(...)
    file: str = Field(...)
    args: Optional[dict[Any, Any]]= Field(default=None) 
    timeout: int = Field(...)
    cpu: int = Field(...)
    memory: int = Field(...)

InputType = Annotated[ 
    Union[HttpInput, BinaryInput, FileInput],
    Field(discriminator="type")
]

class JobConfiguration(BaseModel):
    project: ProjectDetails = Field(...)
    run: RunDetails = Field(...)
    input: InputType = Field(...)
    output: Output = Field(...)
    error: Error = Field(...)
    error_map: dict[str, int] = Field(...)