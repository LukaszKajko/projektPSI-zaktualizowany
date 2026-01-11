from uuid import UUID
from pydantic import BaseModel, ConfigDict

from infrastructure.dto.clubdto import ClubDTO


class StadiumDTO(BaseModel):
    """DTO representing a Stadium entity."""

    stadium_id: int
    name: str
    seats: int
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
            seats=record.get("seats"),
            club=ClubDTO(
                club_id=record.get("club_id"),
                name=record.get("club_name"),
                place_id=record.get("place_id"),
            ),
            user_id=record.get("user_id"),
        )
