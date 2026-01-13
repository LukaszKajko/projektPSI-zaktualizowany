from uuid import UUID
from typing import Iterable

from core.repositories.iticket import ITicketRepository
from core.repositories.istadium import IStadiumRepository
from infrastructure.dto.ticketdto import TicketDTO


class TicketService:

    def __init__(self, ticket_repo: ITicketRepository, stadium_repo: IStadiumRepository):
        self._ticket_repo = ticket_repo
        self._stadium_repo = stadium_repo

    async def buy_ticket(self, user_id: UUID, stadium_id: int) -> TicketDTO:
        stadium = await self._stadium_repo.get_by_id(stadium_id)
        if not stadium:
            raise ValueError("Stadium not found")

        ticket = await self._ticket_repo.buy(
            user_id=user_id,
            stadium_id=stadium_id,
            price=stadium.price,
        )
        return TicketDTO.model_validate(ticket)

    async def get_user_tickets(self, user_id: UUID) -> Iterable[TicketDTO]:
        tickets = await self._ticket_repo.get_by_user(user_id)
        return [TicketDTO.model_validate(t) for t in tickets]
