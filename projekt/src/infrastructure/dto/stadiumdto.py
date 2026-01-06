from uuid import UUID
from pydantic import BaseModel, ConfigDict

from src.infrastructure.dto.clubdto import ClubDTO

class StadiumDTO(BaseModel):
    """DTO representing a Stadium entity."""
    
    stadium_id: int
    name: str
    club: ClubDTO
    user_id: UUID

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
    )

    @classmethod
    def from_record(cls, record: dict) -> "StadiumDTO":
        """Create a StadiumDTO instance from a DB record."""
        return cls(
            stadium_id=record.get("stadium_id"),
            name=record.get("name"),
            club=ClubDTO(
                club_id=record.get("club_id"),
                name=record.get("club_name"),
                place_id=record.get("place_id"),
            ),
            user_id=record.get("user_id"),
        )
