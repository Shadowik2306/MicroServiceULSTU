from typing import Annotated
from pydantic import BaseModel


class SWorkerAdd(BaseModel):
    username: str
    email: str


class SWorkerUpdate(BaseModel):
    id: int
    username: str | None = None
    email: str | None = None

