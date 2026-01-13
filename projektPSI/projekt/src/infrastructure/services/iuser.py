from abc import ABC, abstractmethod
from uuid import UUID

from core.domain.user import User
from infrastructure.dto.userdto import UserDTO
from infrastructure.dto.tokendto import TokenDTO


class IUserService(ABC):
    """User service abstraction."""

    @abstractmethod
    async def register_user(self, data: User) -> UserDTO | None:
        """Register a new user."""
        pass

    @abstractmethod
    async def authenticate_user(self, data: User) -> TokenDTO | None:
        """Authenticate user and return JWT token."""
        pass

    @abstractmethod
    async def get_by_uuid(self, uuid: UUID) -> UserDTO | None:
        """Get user by UUID."""
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> UserDTO | None:
        """Get user by email."""
        pass
