from typing import List, Optional
from asyncpg import Record  # type: ignore

from core.domain.stadium import Stadium
from core.repositories.istadium import IStadiumRepository
from db import stadium_table, database


class StadiumRepository(IStadiumRepository):
    """Database implementation of Stadium repository."""

    async def get_by_id(self, stadium_id: int) -> Optional[Stadium]:
        record = await self._get_by_id(stadium_id)
        return Stadium.model_validate(record) if record else None

    async def get_all(self) -> List[Stadium]:
        query = stadium_table.select().order_by(stadium_table.c.name.asc())
        records = await database.fetch_all(query)
        return [Stadium.model_validate(record) for record in records]

    async def add(self, stadium: Stadium) -> Stadium:
        query = stadium_table.insert().values(
            name=stadium.name,
            club_id=stadium.club_id,
            seats=stadium.seats,
        )
        new_id = await database.execute(query)

        record = await self._get_by_id(new_id)
        return Stadium.model_validate(record)

    async def update(self, stadium_id: int, stadium: Stadium) -> Optional[Stadium]:
        if not await self._get_by_id(stadium_id):
            return None

        query = (
            stadium_table.update()
            .where(stadium_table.c.stadium_id == stadium_id)
            .values(
                name=stadium.name,
                club_id=stadium.club_id,
                seats=stadium.seats,
            )
        )
        await database.execute(query)

        record = await self._get_by_id(stadium_id)
        return Stadium.model_validate(record) if record else None

    async def delete(self, stadium_id: int) -> bool:
        if not await self._get_by_id(stadium_id):
            return False

        query = stadium_table.delete().where(stadium_table.c.stadium_id == stadium_id)
        await database.execute(query)
        return True

    async def _get_by_id(self, stadium_id: int) -> Optional[Record]:
        query = stadium_table.select().where(stadium_table.c.stadium_id == stadium_id)
        return await database.fetch_one(query)
