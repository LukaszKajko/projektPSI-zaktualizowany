from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class SupportMessageDTO(BaseModel):
    message_id: int
    user_id: UUID
    message: str
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )
