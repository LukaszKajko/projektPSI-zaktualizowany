from pydantic import BaseModel, ConfigDict

class ClubDTO(BaseModel):
    """DTO representing a Club entity."""

    club_id: int
    name: str
    place_id: int
    amount_of_points: int

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )
