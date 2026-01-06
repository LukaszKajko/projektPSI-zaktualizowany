"""Module providing containers injecting dependencies."""

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory, Singleton

from src.infrastructure.repositories.user import UserRepository
from src.infrastructure.repositories.clubdb import \
    ClubRepository
from src.infrastructure.repositories.stadiumdb import \
    StadiumRepository


from src.infrastructure.services.club import ClubService
from src.infrastructure.services.stadium import StadiumService
from src.infrastructure.services.user import UserService


class Container(DeclarativeContainer):
    """Container class for dependency injecting purposes."""
    club_repository = Singleton(ClubRepository)
    stadium_repository = Singleton(StadiumRepository)
    user_repository = Singleton(UserRepository)

    club_service = Factory(
        ClubService,
        repository=club_repository,
    )
    stadium_service = Factory(
        StadiumService,
        repository=stadium_repository,
    )
   
    user_service = Factory(
        UserService,
        repository=user_repository,
    )