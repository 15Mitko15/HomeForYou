"""ENV"""

import sys
from os.path import abspath, dirname

sys.path.insert(
    0,
    dirname(dirname(abspath(__file__))),
)

import asyncio
from logging.config import fileConfig
from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine

from src.config import DB_URL
from src.database import Base

# pylint: disable=no-member
# This is the Alembic Config object
config = context.config

# Set up logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set target metadata
target_metadata = Base.metadata


def do_run_migrations(connection):  # type: ignore
    """Function"""
    context.configure(
        connection=connection,  # type: ignore
        target_metadata=target_metadata,
        compare_type=True,
        compare_server_default=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = DB_URL.replace("+asyncpg", "")  # Use sync URL format
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' (async) mode."""
    connectable = create_async_engine(DB_URL)

    async def run_async_migrations():
        async with connectable.connect() as connection:
            await connection.run_sync(do_run_migrations)  # type: ignore

    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
