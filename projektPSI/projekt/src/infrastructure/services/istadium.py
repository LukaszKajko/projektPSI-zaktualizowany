from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterable, Optional

from core.domain.stadium import Stadium
from infrastructure.dto.stadiumdto import StadiumDTO


class IStadiumService(ABC):
    """Service interface for Stadium entity."""

    @abstractmethod
    async def get_all(self) -> Iterable[StadiumDTO]:
        pass

    @abstractmethod
    async def get_by_id(self, stadium_id: int) -> Optional[StadiumDTO]:
        pass

    @abstractmethod
    async def add(self, stadium: Stadium) -> Optional[StadiumDTO]:
        pass

    @abstractmethod
    async def update(self, stadium_id: int, stadium: Stadium) -> Optional[StadiumDTO]:
        pass

    @abstractmethod
    async def delete(self, stadium_id: int) -> bool:
        pass
