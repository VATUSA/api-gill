from fastapi import FastAPI
from loguru import logger


async def open_database_connection(app: FastAPI) -> None:
    logger.info("Connecting to database...")
    await app.state.database.connect()
    logger.info("Connected to database.")


async def close_database_connection(app: FastAPI) -> None:
    logger.info("Closing database connection...")
    await app.state.database.disconnet()
    logger.info("Closed database connection.")
