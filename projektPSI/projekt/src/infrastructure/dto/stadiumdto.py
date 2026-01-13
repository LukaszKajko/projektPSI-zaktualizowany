from decimal import Decimal
from pydantic import BaseModel, ConfigDict

class StadiumDTO(BaseModel):
    stadium_id: int
    name: str
    club_id: int
    seats: int
    price: Decimal
    draft: str | None = None

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )
