from uuid import UUID
from typing import Optional

from infrastructure.utils.password import hash_password
from core.domain.user import User
from core.repositories.iuser import IUserRepository
from db import database, user_table


class UserRepository(IUserRepository):
    """Database implementation of User repository."""

    async def register_user(self, user: User) -> Optional[User]:
        # Check if user already exists
        if await self.get_by_email(user.email):
            return None

        password_hash = hash_password(user.password_hash)

        query = user_table.insert().values(
            email=user.email,
            password_hash=password_hash,
            is_active=user.is_active,
        )

        new_user_id: UUID = await database.execute(query)
        return await self.get_by_uuid(new_user_id)

    async def get_by_uuid(self, user_id: UUID) -> Optional[User]:
        query = user_table.select().where(user_table.c.user_id == user_id)
        record = await database.fetch_one(query)

        if not record:
            return None

        return User.model_validate(record)

    async def get_by_email(self, email: str) -> Optional[User]:
        query = user_table.select().where(user_table.c.email == email)
        record = await database.fetch_one(query)

        if not record:
            return None

        return User.model_validate(record)
