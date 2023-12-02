from asyncio import current_task
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_scoped_session
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from settings import settings

CONNECTION_STRING = f"postgresql+asyncpg://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"

engine = create_async_engine(
    CONNECTION_STRING,
    echo=True,
    future=True,
)

sessionmaker = async_sessionmaker(bind=engine)

scoped_session = async_scoped_session(session_factory=sessionmaker, scopefunc=current_task)


async def get_scoped_session() -> AsyncGenerator[AsyncSession, None]:
    async with scoped_session() as session:
        yield session
        await scoped_session.remove()
