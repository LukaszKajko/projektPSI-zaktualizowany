from uuid import UUID
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict

class Ticket(BaseModel):
    ticket_id: int
    user_id: UUID
    stadium_id: int
    price: Decimal
    purchased_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )
