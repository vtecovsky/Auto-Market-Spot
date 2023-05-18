from pydantic import BaseModel


class Item(BaseModel):
    id: int
    price: float
    figi: str
    type: str
