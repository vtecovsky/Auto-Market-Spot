"""
Подключение к БД. Взято из документации. Сам ничего не писал
"""
from typing import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER


"""
Подключение к БД
"""

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
Base = declarative_base()

"""
Некоторые поля класса взяты из документации, некоторые из моей модели пользователя для БД
"""
engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


"""
Создает связь между БД и аутентификацией юзеров.
"""
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
