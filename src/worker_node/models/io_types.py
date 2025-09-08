from enum import Enum
from typing import Literal, Optional
from pydantic import BaseModel, Field


class IOType(Enum):
    FILE = "file"
    HTTP = "http"
    BIN = "bin"
    STDOUT = "stdout" # used for output and error

class BaseIO(BaseModel):
    type: IOType = Field(...)

class HttpInput(BaseIO):
    type: Literal["http"] # pyright: ignore[reportIncompatibleVariableOverride]
    port: int = Field(...)
    allowed_routes: list[str] = Field(...)
    allowed_methods: list[str] = Field(...)
    health_check: str = Field(...)

class BinaryInput(BaseIO):
    type: Literal["bin"] # pyright: ignore[reportIncompatibleVariableOverride]
    allow_args: bool = Field(...)
    allow_stdin: bool = Field(...)
    allowed_args: list[str] = Field(...)

class FileInput(BaseIO):
    type: Literal["file"] # pyright: ignore[reportIncompatibleVariableOverride]
    path: str = Field(...)

class Output(BaseIO):
    path: Optional[str] = Field(default=None, description="Relative path if file is the type")

class Error(Output): # same as output different names
    ...
 