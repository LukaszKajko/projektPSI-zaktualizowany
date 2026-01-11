"""Main module of the app"""

from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.exception_handlers import http_exception_handler

from api.routers.club import router as club_router
from api.routers.stadium import router as stadium_router
from api.routers.user import router as user_router
from container import Container
from db import database, init_db


container = Container()
container.wire(
    modules=[
        "api.routers.club",
        "api.routers.stadium",
        "api.routers.user",
    ]
)


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator:
    await init_db()
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)

app.include_router(club_router, prefix="/club", tags=["club"])
app.include_router(stadium_router, prefix="/stadium")

app.include_router(user_router, tags=["user"])


@app.exception_handler(HTTPException)
async def http_exception_handle_logging(
    request: Request,
    exception: HTTPException,
) -> Response:
    return await http_exception_handler(request, exception)
