"""A module providing database access."""

import asyncio
import asyncio
from sqlalchemy.exc import OperationalError
import databases
import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.exc import OperationalError, DatabaseError
from sqlalchemy.ext.asyncio import create_async_engine
from asyncpg.exceptions import (    # type: ignore
    CannotConnectNowError,
    ConnectionDoesNotExistError,
)

from config import config

metadata = sqlalchemy.MetaData()

# Stadium table
stadium_table = sqlalchemy.Table(
    "stadiums",
    metadata,
    sqlalchemy.Column("stadium_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("club_id", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("seats", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("price", sqlalchemy.Numeric(10, 2), nullable=False, server_default="0"),
    sqlalchemy.Column("draft", sqlalchemy.String, nullable=True),
)

ticket_table = sqlalchemy.Table(
    "tickets",
    metadata,
    sqlalchemy.Column("ticket_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", UUID(as_uuid=True), nullable=False),
    sqlalchemy.Column("stadium_id", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("price", sqlalchemy.Numeric(10, 2), nullable=False),
    sqlalchemy.Column(
        "purchased_at",
        sqlalchemy.DateTime,
        server_default=sqlalchemy.func.now(),
        nullable=False,
    ),
)



# Club table
club_table = sqlalchemy.Table(
    "clubs",
    metadata,
    sqlalchemy.Column("club_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("place_id", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("amount_of_points", sqlalchemy.Integer, nullable=False, server_default="0"),
)


# User table
user_table = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column(
        "user_id",
        UUID(as_uuid=True),
        primary_key=True,
        server_default=sqlalchemy.text("gen_random_uuid()"),
    ),
    sqlalchemy.Column("email", sqlalchemy.String, unique=True, nullable=False),
    sqlalchemy.Column("password_hash", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("is_active", sqlalchemy.Boolean, nullable=False, server_default="true"),
)

# Support
support_table = sqlalchemy.Table(
    "support_messages",
    metadata,
    sqlalchemy.Column("message_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", UUID(as_uuid=True), nullable=False),
    sqlalchemy.Column("message", sqlalchemy.Text, nullable=False),
    sqlalchemy.Column(
        "created_at",
        sqlalchemy.DateTime,
        server_default=sqlalchemy.func.now(),
        nullable=False,
    ),
)


# Database URI
db_uri = (
    f"postgresql+asyncpg://{config.DB_USER}:{config.DB_PASSWORD}"
    f"@{config.DB_HOST}/{config.DB_NAME}"
)

engine = create_async_engine(
    db_uri,
    echo=True,
    future=True,
    pool_pre_ping=True,
)

database = databases.Database(db_uri, force_rollback=False)



async def init_db():
    retries = 10
    for attempt in range(retries):
        try:
            async with engine.begin() as conn:
                await conn.run_sync(metadata.create_all)
            print("Database initialized.")
            return
        except OperationalError:
            print(f"Database not ready, retrying... ({attempt+1}/{retries})")
            await asyncio.sleep(2)

    raise Exception("Database connection failed after retries")

