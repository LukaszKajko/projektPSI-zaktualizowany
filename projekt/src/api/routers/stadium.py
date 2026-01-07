"""A module containing stadium endpoints."""

from typing import Iterable
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from src.container import Container
from src.core.domain.stadium import Stadium, StadiumIn
from src.infrastructure.services.istadium import IStadiumService

router = APIRouter()


@router.post("/create", response_model=Stadium, status_code=201)
@inject
async def create_stadium(
    stadium: StadiumIn,
    service: IStadiumService = Depends(Provide[Container.stadium_service]),
) -> Stadium:
    new_stadium = await service.add_stadium(stadium)
    if not new_stadium:
        raise HTTPException(status_code=400, detail="Cannot create stadium")
    return new_stadium


@router.get("/all", response_model=list[Stadium])
@inject
async def get_all_stadiums(
    service: IStadiumService = Depends(Provide[Container.stadium_service]),
) -> list[Stadium]:
    return await service.get_all_stadiums()


@router.get("/{stadium_id}", response_model=Stadium)
@inject
async def get_stadium_by_id(
    stadium_id: int,
    service: IStadiumService = Depends(Provide[Container.stadium_service]),
) -> Stadium:
    stadium = await service.get_stadium_by_id(stadium_id)
    if not stadium:
        raise HTTPException(status_code=404, detail="Stadium not found")
    return stadium


@router.put("/{stadium_id}", response_model=Stadium)
@inject
async def update_stadium(
    stadium_id: int,
    stadium: StadiumIn,
    service: IStadiumService = Depends(Provide[Container.stadium_service]),
) -> Stadium:
    updated = await service.update_stadium(stadium_id, stadium)
    if not updated:
        raise HTTPException(status_code=404, detail="Stadium not found")
    return updated


@router.delete("/{stadium_id}", status_code=204)
@inject
async def delete_stadium(
    stadium_id: int,
    service: IStadiumService = Depends(Provide[Container.stadium_service]),
) -> None:
    deleted = await service.delete_stadium(stadium_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Stadium not found")
