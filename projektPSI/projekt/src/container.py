"""Module providing containers injecting dependencies."""

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory, Singleton

from infrastructure.repositories.user import UserRepository
from infrastructure.repositories.clubdb import ClubRepository
from infrastructure.repositories.stadiumdb import StadiumRepository

from infrastructure.services.club import ClubService
from infrastructure.services.stadium import StadiumService
from infrastructure.services.user import UserService
from infrastructure.repositories.ticketdb import TicketRepository
from infrastructure.services.ticket import TicketService
from infrastructure.repositories.supportdb import SupportRepository
from infrastructure.services.support import SupportService

class Container(DeclarativeContainer):
    """Container class for dependency injecting purposes."""

    # Repositories
    club_repository = Singleton(ClubRepository)
    stadium_repository = Singleton(StadiumRepository)
    user_repository = Singleton(UserRepository)
    ticket_repository = Singleton(TicketRepository)
    support_repository = Singleton(SupportRepository)
    # Services
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

    ticket_service = Factory(
        TicketService,
        ticket_repo=ticket_repository,
        stadium_repo=stadium_repository,
    )

    support_service = Factory(
        SupportService,
        repository=support_repository,
    )


