from pydantic import BaseModel, ConfigDict

class Club(BaseModel):
    club_id: int | None = None
    name: str
    place_id: int
    amount_of_points: int


    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )
