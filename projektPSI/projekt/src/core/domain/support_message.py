from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class SupportMessage(BaseModel):
    message_id: int | None = None
    user_id: UUID
    message: str
    created_at: datetime | None = None

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )
