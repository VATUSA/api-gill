import os

import databases
import sqlalchemy
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from app.v1.core.events import start_app_handler
from app.v1.core.events import stop_app_handler

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

    metadata = sqlalchemy.MetaData()
    database = databases.Database(os.getenv("DATABASE_URL"))
    api.state.database = database
    api.state.metadata = metadata
    api.add_event_handler("startup", start_app_handler(api))
    api.add_event_handler("shutdown", stop_app_handler(api))

    return api


api = create_app()
