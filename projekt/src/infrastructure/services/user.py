from pydantic import UUID4

from src.core.domain.user import UserIn, User
from src.core.repositories.iuser import IUserRepository
from src.infrastructure.dto.userdto import UserDTO
from src.infrastructure.dto.tokendto import TokenDTO
from src.infrastructure.services.iuser import IUserService
from src.infrastructure.utils.password import verify_password
from src.infrastructure.utils.token import generate_user_token


class UserService(IUserService):
    """User service implementation."""

    def __init__(self, repository: IUserRepository) -> None:
        self._repository = repository

    async def register_user(self, user: UserIn) -> UserDTO | None:
        created_user: User | None = await self._repository.register_user(user)
        if not created_user:
            return None

        return UserDTO.model_validate(created_user)

    async def authenticate_user(self, user: UserIn) -> TokenDTO | None:
        user_data: User | None = await self._repository.get_by_email(user.email)
        if not user_data:
            return None

        if not verify_password(user.password, user_data.password_hash):
            return None

        token_details = generate_user_token(user_data.id)
        return TokenDTO(token_type="Bearer", **token_details)

    async def get_by_uuid(self, uuid: UUID4) -> UserDTO | None:
        user = await self._repository.get_by_uuid(uuid)
        return UserDTO.model_validate(user) if user else None

    async def get_by_email(self, email: str) -> UserDTO | None:
        user = await self._repository.get_by_email(email)
        return UserDTO.model_validate(user) if user else None
