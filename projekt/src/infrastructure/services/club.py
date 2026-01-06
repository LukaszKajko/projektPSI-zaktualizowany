from typing import List, Optional

from src.core.domain.club import Club, ClubIn
from src.core.repositories.iclub import IClubRepository
from src.infrastructure.services.iclub import IClubService

class ClubService(IClubService):
    """Service class for Club entity."""

    def __init__(self, repository: IClubRepository) -> None:
        """Initialize the club service with a repository."""
        self._repository = repository

    async def get_by_id(self, club_id: int) -> Optional[Club]:
        """Get a club by its ID."""
        return await self._repository.get_by_id(club_id)

    async def get_all(self) -> List[Club]:
        """Get all clubs."""
        return await self._repository.get_all()

    async def add(self, club: ClubIn) -> Optional[Club]:
        """Add a new club."""
        return await self._repository.add(club)

    async def update(self, club_id: int, club: ClubIn) -> Optional[Club]:
        """Update an existing club."""
        return await self._repository.update(club_id, club)

    async def delete(self, club_id: int) -> bool:
        """Delete a club by ID."""
        return await self._repository.delete(club_id)
