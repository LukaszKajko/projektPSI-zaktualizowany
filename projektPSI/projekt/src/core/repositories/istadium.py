from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable

from core.domain.stadium import Stadium

class IStadiumRepository(ABC):
    """Repository interface for Stadium entity."""

    @abstractmethod
    async def get_all(self) -> Iterable[Stadium]:
        """Return all stadiums from the data storage."""
        pass

    @abstractmethod
    async def get_by_id(self, stadium_id: int) -> Stadium | None:
        """Return a stadium by its ID, or None if not found."""
        pass

    @abstractmethod
    async def get_by_name(self, stadium_name: str) -> Stadium | None:
        """Return a stadium by its name, or None if not found."""
        pass

    @abstractmethod
    async def get_by_club_name(self, club_name: str) -> Stadium | None:
        """Return a stadium by the club's name, or None if not found."""
        pass

    @abstractmethod
    async def get_by_user(self, user_id: int) -> Iterable[Stadium]:
        """Return stadiums added by a specific user."""
        pass

    @abstractmethod
    async def add(self, stadium: Stadium) -> Stadium:
        """Add a new stadium to the data storage."""
        pass

    @abstractmethod
    async def update(self, stadium_id: int, stadium: Stadium) -> Stadium | None:
        """Update an existing stadium and return the updated entity, or None if not found."""
        pass

    @abstractmethod
    async def delete(self, stadium_id: int) -> bool:
        """Delete a stadium by ID. Returns True if deleted, False otherwise."""
        pass
