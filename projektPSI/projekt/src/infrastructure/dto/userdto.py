from uuid import UUID
from pydantic import BaseModel, ConfigDict

class UserDTO(BaseModel):
    """DTO representing a User entity."""
    
    user_id: UUID
    email: str

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )
