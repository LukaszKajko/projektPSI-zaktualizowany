from uuid import UUID

from core.domain.user import User
from core.repositories.iuser import IUserRepository
from infrastructure.dto.userdto import UserDTO
from infrastructure.dto.tokendto import TokenDTO
from infrastructure.services.iuser import IUserService
from infrastructure.utils.password import verify_password
from infrastructure.utils.token import generate_user_token


class UserService(IUserService):
    """User service implementation."""

    def __init__(self, repository: IUserRepository) -> None:
        self._repository = repository

    async def register_user(self, user: User) -> UserDTO | None:
        """Register a new user."""
        created_user = await self._repository.register_user(user)
        if not created_user:
            return None

        return UserDTO.model_validate(created_user)

    async def authenticate_user(self, user: User) -> TokenDTO | None:
        """Authenticate a user and generate a token."""

        # Pobierz użytkownika po emailu
        user_data = await self._repository.get_by_email(user.email)
        if not user_data:
            return None

        # Weryfikacja hasła: plain vs hashed
        if not verify_password(user.password_hash, user_data.password_hash):
            return None

        # Generowanie tokenu
        token_details = generate_user_token(user_data.user_id)

        return TokenDTO(
            token_type="Bearer",
            **token_details
        )

    async def get_by_uuid(self, uuid: UUID) -> UserDTO | None:
        """Get a user by UUID."""
        user = await self._repository.get_by_uuid(uuid)
        return UserDTO.model_validate(user) if user else None

    async def get_by_email(self, email: str) -> UserDTO | None:
        """Get a user by email."""
        user = await self._repository.get_by_email(email)
        return UserDTO.model_validate(user) if user else None
