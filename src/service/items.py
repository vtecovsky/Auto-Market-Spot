from select import select

from fastapi import Depends
from sqlalchemy import delete, insert, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.items import CreateItemScheme, ViewItemScheme
from src.storage.database import get_async_session
from src.storage.models.items import Item as ItemModel


class ItemService:
    @staticmethod
    async def add_specific_item(
        data: CreateItemScheme, session: AsyncSession = Depends(get_async_session)
    ) -> ViewItemScheme:
        query = insert(ItemModel).values(**data.dict()).returning(ItemModel)
        obj = await session.scalar(query)
        await session.commit()
        if obj:
            return ViewItemScheme.from_orm(obj)

    @staticmethod
    async def get_specific_item(
        item_id: int, session: AsyncSession = Depends(get_async_session)
    ) -> ViewItemScheme:
        query = select(ItemModel).where(ItemModel.id == item_id).returning(ItemModel)
        obj = await session.scalar(query)
        if obj:
            return ViewItemScheme.from_orm(obj)

    @staticmethod
    async def update_specific_item(
        item_id: int,
        updated_item: ViewItemScheme,
        session: AsyncSession = Depends(get_async_session),
    ) -> ViewItemScheme:
        query = (
            update(ItemModel)
            .where(ItemModel.id == item_id)
            .values(**updated_item.dict())
            .returning(ItemModel)
        )
        obj = await session.scalar(query)
        await session.commit()
        if obj:
            return ViewItemScheme.from_orm(obj)

    @staticmethod
    async def delete_specific_item(
        item_id: int, session: AsyncSession = Depends(get_async_session)
    ) -> None:
        query = delete(ItemModel).where(ItemModel.id == item_id)
        await session.execute(query)
        await session.commit()
