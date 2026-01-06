from typing import Iterable

from src.core.domain.stadium import Stadium, StadiumBroker
from src.core.repositories.istadium import IStadiumRepository
from src.infrastructure.dto.stadiumdto import StadiumDTO
from src.infrastructure.services.istadium import IStadiumService


class StadiumService(IStadiumService):
    """Stadium service implementation."""

    def __init__(self, repository: IStadiumRepository) -> None:
        self._repository = repository

    async def get_all(self) -> Iterable[StadiumDTO]:
        stadiums = await self._repository.get_all_stadiums()
        return [StadiumDTO.model_validate(s) for s in stadiums]

    async def get_by_stadiumName(self, stadiumName: str) -> StadiumDTO | None:
        stadium = await self._repository.get_by_stadiumName(stadiumName)
        return StadiumDTO.model_validate(stadium) if stadium else None

    async def get_by_clubName(self, clubName: str) -> StadiumDTO | None:
        stadium = await self._repository.get_by_clubName(clubName)
        return StadiumDTO.model_validate(stadium) if stadium else None

    async def get_by_user(self, user_id: int) -> Iterable[StadiumDTO]:
        stadiums = await self._repository.get_by_user(user_id)
        return [StadiumDTO.model_validate(s) for s in stadiums]

    async def add_stadium(self, data: StadiumBroker) -> Stadium | None:
        return await self._repository.add_stadium(data)

    async def update_stadium(
        self,
        stadiumId: int,
        data: StadiumBroker,
    ) -> Stadium | None:
        return await self._repository.update_stadium(
            stadiumsId=stadiumId,
            data=data,
        )

    async def delete_stadium(self, stadiumId: int) -> bool:
        return await self._repository.delete_stadium(stadiumId)
