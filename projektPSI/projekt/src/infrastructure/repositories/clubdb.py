from db import club_table, database
from core.domain.club import Club
from core.repositories.iclub import IClubRepository


class ClubRepository(IClubRepository):

    async def add(self, club: Club) -> Club | None:
        query = club_table.insert().values(
            name=club.name,
            place_id=club.place_id,
            amount_of_points=club.amount_of_points,
        )
        club_id = await database.execute(query)
        return Club(club_id=club_id, **club.model_dump(exclude={"club_id"}))

    async def get_all(self) -> list[Club]:
        rows = await database.fetch_all(club_table.select())
        return [Club(**row) for row in rows]

    async def get_by_id(self, club_id: int) -> Club | None:
        row = await database.fetch_one(
            club_table.select().where(club_table.c.club_id == club_id)
        )
        return Club(**row) if row else None

    async def update(self, club_id: int, club: Club) -> Club | None:
        query = (
            club_table.update()
            .where(club_table.c.club_id == club_id)
            .values(
                name=club.name,
                place_id=club.place_id,
                amount_of_points=club.amount_of_points,
            )
        )
        await database.execute(query)
        return await self.get_by_id(club_id)

    async def delete(self, club_id: int) -> bool:
        result = await database.execute(
            club_table.delete().where(club_table.c.club_id == club_id)
        )
        return bool(result)

    async def get_ranking(self) -> list[Club]:
        query = club_table.select().order_by(club_table.c.amount_of_points.desc())
        rows = await database.fetch_all(query)
        return [Club(**row) for row in rows]

