from fastapi import Depends
from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.items import router
from src.items.models import Item as ItemModel
from src.items.schemas import Item


@router.get("/")
async def get_specific_item(
    item_name: str, session: AsyncSession = Depends(get_async_session)
):
    query = select(ItemModel).where(ItemModel.figi == item_name)
    result_proxy = await session.execute(query)
    result = result_proxy.fetchall()

    # Extract column names from the table
    columns = result_proxy.keys()

    # Convert the result to a list of dictionaries
    result_dict = [dict(zip(columns, row)) for row in result]

    return result_dict


@router.post("/{item_id}")
async def add_specific_item(
    new_item: Item, session: AsyncSession = Depends(get_async_session)
):
    stmt = insert(ItemModel).values(**new_item.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.put("/{item_id}")
async def update_specific_item(
    item_id: int, updated_item: Item, session: AsyncSession = Depends(get_async_session)
):
    stmt = (
        update(ItemModel).where(ItemModel.id == item_id).values(**updated_item.dict())
    )
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.delete("/{item_id}")
async def delete_specific_item(
    item_id: int, session: AsyncSession = Depends(get_async_session)
):
    query = delete(ItemModel).where(ItemModel.id == item_id)
    await session.execute(query)
    await session.commit()
    return {"status": "success"}
