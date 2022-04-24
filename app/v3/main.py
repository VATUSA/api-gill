import os

import sentry_sdk
from dotenv import load_dotenv
from fastapi import FastAPI
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from app.v3.core.events import start_app_handler
from app.v3.core.events import stop_app_handler
from app.v3.database.connection import database
from app.v3.database.connection import metadata
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


if os.getenv("DEBUG", "false") == "true":
    api = create_app()
else:
    sentry_sdk.init(dsn=os.getenv("SENTRY_DSN"))
    api = SentryAsgiMiddleware(create_app())
