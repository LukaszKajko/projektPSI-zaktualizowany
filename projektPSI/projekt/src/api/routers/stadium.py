"""A module containing stadium endpoints."""

from typing import List
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from container import Container
from core.domain.stadium import Stadium
from infrastructure.services.istadium import IStadiumService

router = APIRouter()


# --- STATIC ROUTES FIRST (no conflicts) ---

@router.post("/create", response_model=Stadium, status_code=201)
@inject
async def create_stadium(
    stadium: Stadium,
    service: IStadiumService = Depends(Provide[Container.stadium_service]),
) -> Stadium:
    """Create a new stadium."""
    new_stadium = await service.add(stadium)
    if not new_stadium:
        raise HTTPException(status_code=400, detail="Cannot create stadium")
    return new_stadium


@router.get("/all", response_model=List[Stadium])
@inject
async def get_all_stadiums(
    service: IStadiumService = Depends(Provide[Container.stadium_service]),
) -> List[Stadium]:
    """Get all stadiums."""
    return await service.get_all()


# --- DYNAMIC ROUTES WITH PREFIX TO AVOID COLLISIONS ---

@router.get("/id/{stadium_id}", response_model=Stadium)
@inject
async def get_stadium_by_id(
    stadium_id: int,
    service: IStadiumService = Depends(Provide[Container.stadium_service]),
) -> Stadium:
    """Get stadium by ID."""
    stadium = await service.get_by_id(stadium_id)
    if not stadium:
        raise HTTPException(status_code=404, detail="Stadium not found")
    return stadium


@router.put("/id/{stadium_id}", response_model=Stadium)
@inject
async def update_stadium(
    stadium_id: int,
    stadium: Stadium,
    service: IStadiumService = Depends(Provide[Container.stadium_service]),
) -> Stadium:
    """Update stadium data."""
    updated = await service.update(stadium_id, stadium)
    if not updated:
        raise HTTPException(status_code=404, detail="Stadium not found")
    return updated


@router.delete("/id/{stadium_id}", status_code=204)
@inject
async def delete_stadium(
    stadium_id: int,
    service: IStadiumService = Depends(Provide[Container.stadium_service]),
) -> None:
    """Delete stadium by ID."""
    deleted = await service.delete(stadium_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Stadium not found")
