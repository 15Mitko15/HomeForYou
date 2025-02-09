"""Connect to db"""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from server.src.config import DATABASE_URL

# Async Engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Async Session Factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False, autoflush=False
)

Base = declarative_base()
