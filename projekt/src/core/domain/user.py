from pydantic import BaseModel, ConfigDict
from uuid import UUID

class User(BaseModel):
    user_id: UUID
    email: str
    password_hash: str
    is_active: bool = True

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )
