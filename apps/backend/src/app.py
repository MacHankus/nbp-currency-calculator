from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from container import Container
from modules.currency.adapters.api.currency_api import router
from settings import settings


class FastApiExtended(FastAPI):
    container: Container

def create_app() -> FastApiExtended:
    container = Container()

    app = FastApiExtended(title=settings.PROJECT_NAME)

    # Set all CORS enabled origins
    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    app.include_router(router)
    app.container = container

    return app
