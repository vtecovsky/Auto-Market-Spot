from sqlalchemy import Table, Column, Integer, String, Float, MetaData

metadata = MetaData()

item = Table(
    "item",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("price", Float),
    Column("figi", String),
    Column("type", String),
)
