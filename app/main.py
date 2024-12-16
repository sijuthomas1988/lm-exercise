from fastapi import FastAPI
from starlette.requests import Request


from app import settings
from app.db.session import Session
from app.routes import router as api_router



def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME, debug=settings.DEBUG,
        version=settings.VERSION
    )
    application.include_router(
        api_router,
    )
    return application


app = get_application()

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = Session()
    response = await call_next(request)
    request.state.db.close()
    return response


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, **settings.LOGGING_CONFIG)