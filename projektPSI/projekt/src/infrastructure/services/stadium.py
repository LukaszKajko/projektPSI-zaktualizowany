from typing import Iterable, Optional

from core.domain.stadium import Stadium
from core.repositories.istadium import IStadiumRepository
from infrastructure.dto.stadiumdto import StadiumDTO
from infrastructure.services.istadium import IStadiumService


class StadiumService(IStadiumService):
    """Stadium service implementation."""

    def __init__(self, repository: IStadiumRepository) -> None:
        self._repository = repository

    async def get_all(self) -> Iterable[StadiumDTO]:
        stadiums = await self._repository.get_all()
        return [StadiumDTO.model_validate(s) for s in stadiums]

    async def get_by_id(self, stadium_id: int) -> Optional[StadiumDTO]:
        stadium = await self._repository.get_by_id(stadium_id)
        return StadiumDTO.model_validate(stadium) if stadium else None

    async def get_by_name(self, stadium_name: str) -> Optional[StadiumDTO]:
        stadium = await self._repository.get_by_name(stadium_name)
        return StadiumDTO.model_validate(stadium) if stadium else None

    async def get_by_club(self, club_id: int) -> Iterable[StadiumDTO]:
        stadiums = await self._repository.get_by_club_name(club_id)
        return [StadiumDTO.model_validate(s) for s in stadiums]

    async def get_by_user(self, user_id: int) -> Iterable[StadiumDTO]:
        stadiums = await self._repository.get_by_user(user_id)
        return [StadiumDTO.model_validate(s) for s in stadiums]

    async def add(self, stadium: Stadium) -> Optional[StadiumDTO]:
        created = await self._repository.add(stadium)
        return StadiumDTO.model_validate(created) if created else None

    async def update(self, stadium_id: int, stadium: Stadium) -> Optional[StadiumDTO]:
        stadium.stadium_id = stadium_id
        updated = await self._repository.update(stadium)
        return StadiumDTO.model_validate(updated) if updated else None

    async def delete(self, stadium_id: int) -> bool:
        return await self._repository.delete(stadium_id)
