from fastapi import FastAPI

from gu_ml.api.routes.router import api_router
from gu_ml.core.event_handlers import start_app_handler, stop_app_handler


def get_app() -> FastAPI:
    gu_app = FastAPI(title="gu-ml", version="v1", debug=True)
    gu_app.include_router(api_router, prefix="/gu-ml")

    gu_app.add_event_handler("startup", start_app_handler(gu_app))
    gu_app.add_event_handler("shutdown", stop_app_handler(gu_app))

    return gu_app


app = get_app()
