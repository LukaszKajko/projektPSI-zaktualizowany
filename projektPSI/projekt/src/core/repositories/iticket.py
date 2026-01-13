from abc import ABC, abstractmethod
from typing import Iterable
from uuid import UUID
from decimal import Decimal

from core.domain.ticket import Ticket

class ITicketRepository(ABC):

    @abstractmethod
    async def buy(self, user_id: UUID, stadium_id: int, price: Decimal) -> Ticket:
        pass

    @abstractmethod
    async def get_by_user(self, user_id: UUID) -> Iterable[Ticket]:
        pass
