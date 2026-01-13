from uuid import UUID
from core.repositories.isupport import ISupportRepository
from infrastructure.dto.supportdto import SupportMessageDTO

class SupportService:

    def __init__(self, repository: ISupportRepository):
        self._repository = repository

    async def send_message(self, user_id: UUID, message: str) -> SupportMessageDTO:
        msg = await self._repository.add(user_id, message)
        return SupportMessageDTO.model_validate(msg)
