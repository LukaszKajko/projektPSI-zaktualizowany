from typing import Iterable
from uuid import UUID
from decimal import Decimal
from asyncpg import Record

from core.domain.ticket import Ticket
from core.repositories.iticket import ITicketRepository
from db import ticket_table, database


class TicketRepository(ITicketRepository):

    async def buy(self, user_id: UUID, stadium_id: int, price: Decimal) -> Ticket:
        query = ticket_table.insert().values(
            user_id=user_id,
            stadium_id=stadium_id,
            price=price,
        )
        new_id = await database.execute(query)
        record = await self._get_by_id(new_id)
        return Ticket.model_validate(record)

    async def get_by_user(self, user_id: UUID) -> Iterable[Ticket]:
        query = ticket_table.select().where(ticket_table.c.user_id == user_id)
        records = await database.fetch_all(query)
        return [Ticket.model_validate(r) for r in records]

    async def _get_by_id(self, ticket_id: int) -> Record:
        query = ticket_table.select().where(ticket_table.c.ticket_id == ticket_id)
        return await database.fetch_one(query)
