from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from items.models import item
from items.schemas import Item

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)


@router.get("/")
async def get_specific_item(item_name: str, session: AsyncSession = Depends(get_async_session)):
    query = select(item).where(item.c.figi == item_name)
    result_proxy = await session.execute(query)
    result = result_proxy.fetchall()

    # Extract column names from the table
    columns = result_proxy.keys()

    # Convert the result to a list of dictionaries
    result_dict = [dict(zip(columns, row)) for row in result]

    return result_dict


@router.post("/{item_id}")
async def add_specific_item(new_item: Item, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(item).values(**new_item.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.put("/{item_id}")
async def update_specific_item(item_id: int, updated_item: Item, session: AsyncSession = Depends(get_async_session)):
    stmt = update(item).where(item.c.id == item_id).values(**updated_item.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.delete("/{item_id}")
async def delete_specific_item(item_id: int, session: AsyncSession = Depends(get_async_session)):
    query = delete(item).where(item.c.id == item_id)
    await session.execute(query)
    await session.commit()
    return {"status": "success"}
