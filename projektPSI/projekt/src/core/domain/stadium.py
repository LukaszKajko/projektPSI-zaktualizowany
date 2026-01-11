from pydantic import BaseModel, ConfigDict

class Stadium(BaseModel):
    stadium_id: int
    name: str
    club_id: int
    seats: int

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )
