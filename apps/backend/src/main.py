import uvicorn

from settings import settings

if __name__ == "__main__":
    uvicorn.run(
        app='app:create_app', host=settings.PROJECT_HOST, port=settings.PROJECT_PORT, reload=True
    )
