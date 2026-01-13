from decimal import Decimal
from pydantic import BaseModel

class StadiumCreate(BaseModel):
    name: str
    club_id: int
    seats: int
    price: Decimal
    draft: str | None = None
