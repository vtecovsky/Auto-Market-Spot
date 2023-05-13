"""
Подключение к БД. Взято из документации. Сам ничего не писал
"""
from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeMeta, declarative_base

from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME


"""
Подключение к БД
"""

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
Base: DeclarativeMeta = declarative_base()

"""
Некоторые поля класса взяты из документации, некоторые из моей модели пользователя для БД
"""
engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


"""
Создает связь между БД и аутентификацией юзеров.
"""
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
