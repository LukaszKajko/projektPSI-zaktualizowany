from datetime import datetime
from pydantic import BaseModel, ConfigDict

class TokenDTO(BaseModel):
    """DTO representing a token for authentication purposes."""
    
    token_type: str
    access_token: str
    expires_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )
