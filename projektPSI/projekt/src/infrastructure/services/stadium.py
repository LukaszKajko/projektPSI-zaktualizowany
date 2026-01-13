from typing import Iterable, Optional

from core.domain.stadium import Stadium
from core.repositories.istadium import IStadiumRepository
from infrastructure.dto.stadiumdto import StadiumDTO
from infrastructure.services.istadium import IStadiumService
from core.domain.stadium_create import StadiumCreate





class StadiumService(IStadiumService):

    def __init__(self, repository: IStadiumRepository):
        self._repository = repository

    async def add(self, stadium: StadiumCreate) -> StadiumDTO:
        created = await self._repository.add(stadium)
        return StadiumDTO.model_validate(created)

    async def get_all(self):
        stadiums = await self._repository.get_all()
        return [StadiumDTO.model_validate(s) for s in stadiums]

    async def get_by_id(self, stadium_id: int):
        stadium = await self._repository.get_by_id(stadium_id)
        return StadiumDTO.model_validate(stadium) if stadium else None


    async def update(self, stadium_id: int, stadium: Stadium):
        updated = await self._repository.update(stadium_id, stadium)
        return StadiumDTO.model_validate(updated) if updated else None

    async def delete(self, stadium_id: int):
        return await self._repository.delete(stadium_id)
