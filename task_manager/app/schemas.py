from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime
from .models import StatusEnum

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: StatusEnum

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    status: Optional[StatusEnum] = None

class TaskOut(BaseModel):
    id: UUID
    title: str
    description: Optional[str]
    status: StatusEnum
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
