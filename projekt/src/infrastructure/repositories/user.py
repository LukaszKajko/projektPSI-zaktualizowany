from uuid import UUID
from typing import Optional

from src.infrastructure.utils.password import hash_password
from src.core.domain.user import User, UserIn
from src.core.repositories.iuser import IUserRepository
from src.db import database, user_table

class UserRepository(IUserRepository):
    """Database implementation of User repository."""

    async def register_user(self, user: UserIn) -> Optional[User]:
        # Sprawdzenie czy użytkownik już istnieje
        if await self.get_by_email(user.email):
            return None

        user.password = hash_password(user.password)
        query = user_table.insert().values(**user.model_dump())
        new_user_uuid = await database.execute(query)

        return await self.get_by_uuid(new_user_uuid)

    async def get_by_uuid(self, user_id: UUID) -> Optional[User]:
        query = user_table.select().where(user_table.c.id == user_id)
        record = await database.fetch_one(query)
        if not record:
            return None

        return User(
            user_id=record["id"],
            email=record["email"],
            password_hash=record["password_hash"],
            is_active=record["is_active"],
        )

    async def get_by_email(self, email: str) -> Optional[User]:
        query = user_table.select().where(user_table.c.email == email)
        record = await database.fetch_one(query)
        if not record:
            return None

        return User(
            user_id=record["id"],
            email=record["email"],
            password_hash=record["password_hash"],
            is_active=record["is_active"],
        )
