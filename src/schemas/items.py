from typing import Optional

from pydantic import BaseModel


class CreateItemScheme(BaseModel):
    price: float
    description: Optional[str] = None
    type: Optional[str] = None


class ViewItemScheme(BaseModel):
    id: int
    price: float
    description: Optional[str] = None
    type: Optional[str] = None

    class Config:
        orm_mode = True
