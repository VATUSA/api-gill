from fastapi import FastAPI
from loguru import logger


async def open_database_connection(api: FastAPI) -> None:
    logger.info("Connecting to database...")
    if not api.state.database.is_connected:
        await api.state.database.connect()
        logger.info("Connected to database")


async def close_database_connection(api: FastAPI) -> None:
    logger.info("Closing database connection...")
    if api.state.database.is_connected:
        await api.state.database.disconnect()
        logger.info("Closed database connection")
