from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.items import router
from src.schemas.items import CreateItemScheme, ViewItemScheme
from src.service.items import ItemService
from src.storage.database import get_async_session


@router.get("/")
async def get_specific_item(
    item_id: int, session: AsyncSession = Depends(get_async_session)
):
    item = await ItemService.get_specific_item(item_id, session)
    return item


@router.post("/{item_id}")
async def add_specific_item(
    new_item: CreateItemScheme, session: AsyncSession = Depends(get_async_session)
):
    created_item = await ItemService.add_specific_item(new_item, session)
    return created_item


@router.put("/{item_id}")
async def update_specific_item(
    item_id: int,
    updated_item: ViewItemScheme,
    session: AsyncSession = Depends(get_async_session),
):
    updated_item = await ItemService.update_specific_item(
        item_id, updated_item, session
    )
    return updated_item


@router.delete("/{item_id}")
async def delete_specific_item(
    item_id: int, session: AsyncSession = Depends(get_async_session)
):
    await ItemService.delete_specific_item(item_id, session)
