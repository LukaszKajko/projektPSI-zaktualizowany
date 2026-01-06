from abc import ABC, abstractmethod
from uuid import UUID

from src.core.domain.user import UserIn
from src.infrastructure.dto.userdto import UserDTO
from src.infrastructure.dto.tokendto import TokenDTO
from src.infrastructure.dto.userlogindto import UserLoginDTO


class IUserService(ABC):
    """User service abstraction."""

    @abstractmethod
    async def register_user(self, data: UserIn) -> UserDTO | None:
        """Register a new user."""
        pass

    @abstractmethod
    async def authenticate_user(self, data: UserLoginDTO) -> TokenDTO | None:
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
