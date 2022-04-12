from fastapi import FastAPI

from app.v3.database.events import close_database_connection
from app.v3.database.events import open_database_connection


async def start_app_handler(app: FastAPI) -> None:
    await open_database_connection(app)


async def stop_app_handler(app: FastAPI) -> None:
    await close_database_connection(app)
