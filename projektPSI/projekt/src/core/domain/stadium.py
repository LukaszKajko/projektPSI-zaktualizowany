from decimal import Decimal
from pydantic import BaseModel, ConfigDict

class Stadium(BaseModel):
    stadium_id: int | None = None
    name: str
    club_id: int
    seats: int
    price: Decimal
    draft: str | None = None

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )
