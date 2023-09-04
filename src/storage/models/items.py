from sqlalchemy import Column, Float, String

from src.storage.__mixin__ import IdMixin
from src.storage.database import Base


class Item(Base, IdMixin):
    __tablename__ = "item"

    price = Column(Float, index=True)
    description = Column(String, index=True)
    type = Column(String, index=True)
