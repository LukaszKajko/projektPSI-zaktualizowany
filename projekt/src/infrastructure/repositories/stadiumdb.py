from typing import List, Optional
from asyncpg import Record  # type: ignore

from src.core.domain.stadium import Stadium, StadiumIn
from src.core.repositories.istadium import IStadiumRepository
from src.db import stadium_table, database

class StadiumRepository(IStadiumRepository):
    """Database implementation of Stadium repository."""

    async def get_by_id(self, stadium_id: int) -> Optional[Stadium]:
        record = await self._get_by_id(stadium_id)
        return Stadium(**dict(record)) if record else None

    async def get_all(self) -> List[Stadium]:
        query = stadium_table.select().order_by(stadium_table.c.name.asc())
        records = await database.fetch_all(query)
        return [Stadium(**dict(record)) for record in records]

    async def add(self, stadium: StadiumIn) -> Stadium:
        query = stadium_table.insert().values(**stadium.model_dump())
        new_id = await database.execute(query)
        record = await self._get_by_id(new_id)
        return Stadium(**dict(record))

    async def update(self, stadium_id: int, stadium: StadiumIn) -> Optional[Stadium]:
        if await self._get_by_id(stadium_id):
            query = (
                stadium_table.update()
                .where(stadium_table.c.id == stadium_id)
                .values(**stadium.model_dump())
            )
            await database.execute(query)
            record = await self._get_by_id(stadium_id)
            return Stadium(**dict(record)) if record else None
        return None

    async def delete(self, stadium_id: int) -> bool:
        if await self._get_by_id(stadium_id):
            query = stadium_table.delete().where(stadium_table.c.id == stadium_id)
            await database.execute(query)
            return True
        return False

    async def _get_by_id(self, stadium_id: int) -> Optional[Record]:
        query = (
            stadium_table.select()
            .where(stadium_table.c.id == stadium_id)
            .order_by(stadium_table.c.name.asc())
        )
        return await database.fetch_one(query)
