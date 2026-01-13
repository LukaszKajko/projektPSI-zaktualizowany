from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable

from core.domain.stadium import Stadium

class IStadiumRepository(ABC):
    """Repository interface for Stadium entity."""

    @abstractmethod
    async def add(self, stadium: Stadium) -> Stadium:
        """Add a new stadium to the data storage."""
        pass

    @abstractmethod
    async def get_all(self) -> Iterable[Stadium]:
        """Return all stadiums from the data storage."""
        pass

    @abstractmethod
    async def get_by_id(self, stadium_id: int) -> Stadium | None:
        """Return a stadium by its ID, or None if not found."""
        pass


    @abstractmethod
    async def update(self, stadium_id: int, stadium: Stadium) -> Stadium | None:
        """Update an existing stadium and return the updated entity, or None if not found."""
        pass

    @abstractmethod
    async def delete(self, stadium_id: int) -> bool:
        """Delete a stadium by ID. Returns True if deleted, False otherwise."""
        pass
