from abc import ABC, abstractmethod
from uuid import UUID
from core.domain.support_message import SupportMessage

class ISupportRepository(ABC):

    @abstractmethod
    async def add(self, user_id: UUID, message: str) -> SupportMessage:
        pass
