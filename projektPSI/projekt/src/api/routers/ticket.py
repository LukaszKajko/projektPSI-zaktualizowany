from uuid import UUID
from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from container import Container
from infrastructure.dto.ticketdto import TicketDTO

router = APIRouter(prefix="/ticket", tags=["ticket"])


@router.get("/buy/{stadium_id}/{user_id}", response_model=TicketDTO)
@inject
async def buy_ticket_get(
    stadium_id: int,
    user_id: UUID,
    ticket_service = Depends(Provide[Container.ticket_service]),
):
    return await ticket_service.buy_ticket(user_id=user_id, stadium_id=stadium_id)


@router.get("/history/{user_id}", response_model=list[TicketDTO])
@inject
async def get_user_tickets(
    user_id: UUID,
    ticket_service = Depends(Provide[Container.ticket_service]),
):
    return await ticket_service.get_user_tickets(user_id=user_id)
