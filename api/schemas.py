from pydantic import BaseModel
from datetime import date


class TodoCreate(BaseModel):
    title: str
    createdAt: date


class Todo(BaseModel):
    id: int
    title: str
    createdAt: date
