from pydantic import BaseModel, ConfigDict

class Club(BaseModel):
    club_id: int
    name: str
    place_id: int

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )
