from abc import ABC, abstractmethod
from uuid import UUID
from typing import Optional

from src.core.domain.user import User

class IUserRepository(ABC):
    """Repository interface for User entity."""

    @abstractmethod
    async def register_user(self, user: User) -> User:
        """Register a new user and return the created User object."""
        pass

    @abstractmethod
    async def get_by_uuid(self, user_id: UUID) -> Optional[User]:
        """Return a user by UUID, or None if not found."""
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> Optional[User]:
        """Return a user by email, or None if not found."""
        pass
