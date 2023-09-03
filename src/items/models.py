from sqlalchemy import Column, Float, Integer, String

from src.database import Base


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Float, index=True)
    figi = Column(String, index=True)
    type = Column(String, index=True)
