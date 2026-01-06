from typing import List, Optional
from asyncpg import Record  # type: ignore

from src.core.domain.club import Club, ClubIn
from src.core.repositories.iclub import IClubRepository
from src.db import club_table, database

class ClubRepository(IClubRepository):
    """Database implementation of Club repository."""

    async def get_by_id(self, club_id: int) -> Optional[Club]:
        record = await self._get_by_id(club_id)
        return Club(**dict(record)) if record else None

    async def get_all(self) -> List[Club]:
        query = club_table.select().order_by(club_table.c.name.asc())
        records = await database.fetch_all(query)
        return [Club(**dict(record)) for record in records]

    async def add(self, club: ClubIn) -> Club:
        query = club_table.insert().values(**club.model_dump())
        new_id = await database.execute(query)
        record = await self._get_by_id(new_id)
        return Club(**dict(record))

    async def update(self, club_id: int, club: ClubIn) -> Optional[Club]:
        if await self._get_by_id(club_id):
            query = (
                club_table.update()
                .where(club_table.c.id == club_id)
                .values(**club.model_dump())
            )
            await database.execute(query)
            record = await self._get_by_id(club_id)
            return Club(**dict(record)) if record else None
        return None

    async def delete(self, club_id: int) -> bool:
        if await self._get_by_id(club_id):
            query = club_table.delete().where(club_table.c.id == club_id)
            await database.execute(query)
            return True
        return False

    async def _get_by_id(self, club_id: int) -> Optional[Record]:
        query = (
            club_table.select()
            .where(club_table.c.id == club_id)
            .order_by(club_table.c.name.asc())
        )
        return await database.fetch_one(query)
