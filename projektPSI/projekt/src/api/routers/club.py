"""A module containing club endpoints."""

from typing import List

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from container import Container
from core.domain.club import Club
from infrastructure.services.iclub import IClubService

router = APIRouter()
@router.get("/ranking", response_model=list[Club])
@inject
async def get_club_ranking(
    service: IClubService = Depends(Provide[Container.club_service]),
) -> list[Club]:
    return await service.get_ranking()


@router.post("/create", response_model=Club, status_code=201)
@inject
async def create_club(
    club: Club,
    service: IClubService = Depends(Provide[Container.club_service]),
) -> Club:
    new_club = await service.add(club)
    if not new_club:
        raise HTTPException(status_code=400, detail="Club not created")
    return new_club


@router.get("/", response_model=List[Club])
@inject
async def get_all_clubs(
    service: IClubService = Depends(Provide[Container.club_service]),
) -> List[Club]:
    return await service.get_all()


@router.get("/{club_id}", response_model=Club)
@inject
async def get_club_by_id(
    club_id: int,
    service: IClubService = Depends(Provide[Container.club_service]),
) -> Club:
    club = await service.get_by_id(club_id)
    if not club:
        raise HTTPException(status_code=404, detail="Club not found")
    return club


@router.put("/{club_id}", response_model=Club)
@inject
async def update_club(
    club_id: int,
    updated_club: Club,
    service: IClubService = Depends(Provide[Container.club_service]),
) -> Club:
    club = await service.update(club_id, updated_club)
    if not club:
        raise HTTPException(status_code=404, detail="Club not found")
    return club


@router.delete("/{club_id}", status_code=204)
@inject
async def delete_club(
    club_id: int,
    service: IClubService = Depends(Provide[Container.club_service]),
) -> None:
    if not await service.delete(club_id):
        raise HTTPException(status_code=404, detail="Club not found")

