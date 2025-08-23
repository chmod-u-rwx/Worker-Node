from typing import Any
from pydantic import BaseModel

class JobRequestPayload(BaseModel):
    type: str
    data: Any