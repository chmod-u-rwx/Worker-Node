from typing import Any, Literal
from pydantic import BaseModel, Field

class SupportedRuntimes():
    PYTHON = "python"
    NODE = "node"
    DOTNET = "dotnet"

class ProjectDetails(BaseModel):
    name: str = Field(...)  
    description: str = Field(...)  
    version: str = Field(...)  
    owner: str = Field(...)  

class RunDetails(BaseModel):
    runtime: Literal["python", "npm", "dotnet"] = Field()
    file: str = Field()
    args: dict[Any, Any]= Field() 
    timeout: int = Field()
    cpu: int = Field()
    memory: int = Field()

class BaseInput(BaseModel):
    type: Literal["file", "http", "bin"] = Field(...)

class HttpInput(BaseInput):
    allowed_routes: list[str] = Field(...)
    allowed_methods: list[str] = Field(...)
    health_check: str = Field(...)
    

class JobConfiguration(BaseModel):
    project: ProjectDetails = Field(...)
    run: RunDetails = Field(...)