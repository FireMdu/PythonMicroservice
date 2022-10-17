from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field

__all__ = [
    "Account"
]


class Account(BaseModel):
    account_id: Optional[int]
    account_number: str
    active: bool = True
    registration_date: datetime = Field(default_factory=lambda: datetime.utcnow())

    class Config:
        orm_mode = True
