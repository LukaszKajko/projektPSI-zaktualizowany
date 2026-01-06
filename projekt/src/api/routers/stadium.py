"""A module containing stadium endpoints."""

from typing import Iterable
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

from src.container import Container
from src.core.domain.stadium import Stadium, StadiumIn
from src.infrastructure.services.istadium import IStadiumService

router = APIRouter()


@router.post("/create", response_model=Stadium, status_code=200)
@inject
async def create_stadium(
    stadium: StadiumIn,
    service: IStadiumService = Depends(Provide[Container.stadium_service]),
) -> Stadium:
    """An endpoint for adding new stadium.

    Args:
        stadium (StadiumIn): The stadium data.
        service (IStadiumService, optional): The injected service dependency.

    Returns:
        dict: The new stadium attributes.
    """

    stadium = await service.add_stadium(stadium)

    if not stadium:
        raise HTTPException(400, "Cannot create stadium")
    return stadium


@router.get("/all", response_model=Iterable[Stadium], status_code=200)
@inject
async def get_all_stadiums(
    service: IStadiumService = Depends(Provide[Container.stadium_service]),
) -> list[Stadium]:
    """An endpoint for getting all stadiums.

    Args:
        service (IStadiumService, optional): The injected service dependency.

    Returns:
        Iterable: The stadium attributes collection.
    """

    return await service.get_all_stadiums()

@router.get("/{stadiumsId}", response_model=Stadium, status_code=200)
@inject
async def get_stadium_by_id(
    stadiumsId: int,
    service: IStadiumService = Depends(Provide[Container.stadium_service]),
) -> dict:
    """An endpoint for getting stadium details by id.

    Args:
        stadiumsId (int): The id of the stadium.
        service (IStadiumService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if stadium does not exist.

    Returns:
        dict: The requested stadium attributes.
    """

    if stadium := await service.get_stadium_by_id(stadiumsId):
        return stadium

    raise HTTPException(status_code=404, detail="Stadium not found")


@router.put("/{stadiumsId}", response_model=Stadium, status_code=201)
@inject
async def update_stadium(
    stadiumsId: int,
    stadium: StadiumIn,
    service: IStadiumService = Depends(Provide[Container.stadium_service]),
) -> dict:
    """An endpoint for updating stadium data.

    Args:
        stadiumsId (int): The id of the stadium.
        updated_stadium (stadiumIn): The updated stadium details.
        service (IStadiumService, optional): The injected service dependency.

    Raises:
        HTTPException: 404 if stadium does not exist.

    Returns:
        dict: The updated stadium details.
    """

    updated = await service.update_stadium(stadiumsId, stadium)
    if not updated:
        raise HTTPException(404, "Stadium not found")
    return updated


@router.delete("/{stadiumsId}", status_code=204)
@inject
async def delete_stadium(
    stadiumsId: int,
    service: IStadiumService = Depends(Provide[Container.stadium_service]),
) -> None:
    """An endpoint for deleting stadiums.

    Args:
        stadiumsId (int): The id of the stadium.
        service (IStadiumService): The injected service dependency.

    Raises:
        HTTPException: 404 if stadium does not exist.

    Returns:
        dict: Empty if operation finished.
    """

    if await service.get_stadium_by_id(stadiumsId=stadiumsId):
        await service.delete_stadium(stadiumsId)
        return

    raise HTTPException(status_code=404, detail="Stadium not found")
