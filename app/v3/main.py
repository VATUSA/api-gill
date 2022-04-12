import os

import databases
import sqlalchemy
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from app.v3.core.events import start_app_handler
from app.v3.core.events import stop_app_handler
from app.v3.routers.user_router import user_router

load_dotenv()


def create_app() -> FastAPI:
    api = FastAPI()
    api.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    if os.getenv("ENVIRONMENT", "local") == "local":
        @api.get("/", include_in_schema=False)
        def redirect_to_swagger() -> RedirectResponse:
            return RedirectResponse("/docs")

    @api.get("/health", include_in_schema=False)
    def health_check() -> str:
        return "OK"
    database_user = os.getenv("DATABASE_USER")
    database_password = os.getenv("DATABASE_PASSWORD")
    database_host = os.getenv("DATABASE_HOST")
    database_port = os.getenv("DATABASE_PORT")
    database_database = os.getenv("DATABASE_DATABASE")

    metadata = sqlalchemy.MetaData()
    database = databases.Database(
        f"postgresql://{database_user}:{database_password}@{database_host}:{database_port}/{database_database}",
    )
    api.state.database = database
    api.state.metadata = metadata

    @api.on_event("startup")
    async def startup() -> None:
        await start_app_handler(api)

    @api.on_event("shutdown")
    async def shutdown() -> None:
        await stop_app_handler(api)

    api.include_router(user_router)

    return api


api = create_app()
