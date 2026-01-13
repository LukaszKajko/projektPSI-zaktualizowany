from uuid import UUID
from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from container import Container
from infrastructure.dto.supportdto import SupportMessageDTO

router = APIRouter(prefix="/support", tags=["support"])

@router.post("/send", response_model=SupportMessageDTO)
@inject
async def send_support_message(
    user_id: UUID,
    message: str,
    support_service = Depends(Provide[Container.support_service]),
):
    return await support_service.send_message(user_id=user_id, message=message)
