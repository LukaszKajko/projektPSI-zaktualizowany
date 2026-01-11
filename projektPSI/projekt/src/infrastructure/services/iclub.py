from abc import ABC, abstractmethod
from typing import List, Optional

from core.domain.club import Club


class IClubService(ABC):
    """Abstract service interface for Club entity."""

    @abstractmethod
    async def get_by_id(self, club_id: int) -> Optional[Club]:
        """Get a club by its ID."""
        pass

    @abstractmethod
    async def get_all(self) -> List[Club]:
        """Get all clubs."""
        pass

    @abstractmethod
    async def add(self, club: Club) -> Optional[Club]:
        """Add a new club."""
        pass

    @abstractmethod
    async def update(self, club_id: int, club: Club) -> Optional[Club]:
        """Update an existing club."""
        pass

    @abstractmethod
    async def delete(self, club_id: int) -> bool:
        """Delete a club by ID."""
        pass

    @abstractmethod
    async def get_ranking(self) -> list[Club]:
        pass

