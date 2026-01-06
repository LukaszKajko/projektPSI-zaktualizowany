from abc import ABC, abstractmethod
from typing import Iterable, Optional

from src.infrastructure.dto.stadiumdto import StadiumDTO
from src.core.domain.stadium import StadiumBroker


class IStadiumService(ABC):
    """Stadium service abstraction (infrastructure layer)."""

    @abstractmethod
    async def get_all(self) -> Iterable[StadiumDTO]:
        """Get all stadiums."""
        pass

    @abstractmethod
    async def get_by_id(self, stadium_id: int) -> Optional[StadiumDTO]:
        """Get stadium by ID."""
        pass

    @abstractmethod
    async def get_by_name(self, stadium_name: str) -> Optional[StadiumDTO]:
        """Get stadium by name."""
        pass

    @abstractmethod
    async def get_by_club(self, club_id: int) -> Iterable[StadiumDTO]:
        """Get stadiums assigned to a club."""
        pass

    @abstractmethod
    async def get_by_user(self, user_id: int) -> Iterable[StadiumDTO]:
        """Get stadiums added by a user."""
        pass

    @abstractmethod
    async def add(self, data: StadiumBroker) -> Optional[StadiumDTO]:
        """Add a new stadium."""
        pass

    @abstractmethod
    async def update(
        self,
        stadium_id: int,
        data: StadiumBroker,
    ) -> Optional[StadiumDTO]:
        """Update stadium."""
        pass

    @abstractmethod
    async def delete(self, stadium_id: int) -> bool:
        """Delete stadium."""
        pass
