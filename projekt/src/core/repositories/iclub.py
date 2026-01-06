from abc import ABC, abstractmethod
from typing import Iterable

from src.core.domain.club import Club


class IClubRepository(ABC):
    """Repository interface for Club entity."""

    @abstractmethod
    async def get_by_id(self, club_id: int) -> Club | None:
        pass

    @abstractmethod
    async def get_all(self) -> Iterable[Club]:
        pass

    @abstractmethod
    async def add(self, club: Club) -> Club:
        pass

    @abstractmethod
    async def update(self, club: Club) -> Club | None:
        pass

    @abstractmethod
    async def delete(self, club_id: int) -> bool:
        pass
