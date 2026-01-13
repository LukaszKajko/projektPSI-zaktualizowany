from core.repositories.iclub import IClubRepository
from core.domain.club import Club
from infrastructure.services.iclub import IClubService


class ClubService(IClubService):
    def __init__(self, repository: IClubRepository):
        self._repository = repository

    async def add(self, club: Club) -> Club | None:
        return await self._repository.add(club)

    async def get_all(self) -> list[Club]:
        return await self._repository.get_all()

    async def get_by_id(self, club_id: int) -> Club | None:
        return await self._repository.get_by_id(club_id)

    async def update(self, club_id: int, club: Club) -> Club | None:
        return await self._repository.update(club_id, club)

    async def delete(self, club_id: int) -> bool:
        return await self._repository.delete(club_id)

    async def get_ranking(self) -> list[Club]:
        return await self._repository.get_ranking()
