"""A module containing user-related routers."""

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from container import Container
from core.domain.user import User
from infrastructure.dto.tokendto import TokenDTO
from infrastructure.dto.userdto import UserDTO
from infrastructure.services.iuser import IUserService

router = APIRouter()


@router.post("/register", response_model=UserDTO, status_code=201)
@inject
async def register_user(
    user: User,
    service: IUserService = Depends(Provide[Container.user_service]),
) -> UserDTO:
    """Register a new user."""
    new_user = await service.register_user(user)
    if not new_user:
        raise HTTPException(
            status_code=400,
            detail="The user with provided e-mail already exists",
        )
    return new_user


@router.post("/token", response_model=TokenDTO, status_code=200)
@inject
async def authenticate_user(
    user: User,
    service: IUserService = Depends(Provide[Container.user_service]),
) -> TokenDTO:
    """Authenticate user and return token."""
    token_details = await service.authenticate_user(user)
    if not token_details:
        raise HTTPException(
            status_code=401,
            detail="Provided incorrect credentials",
        )
    return token_details
