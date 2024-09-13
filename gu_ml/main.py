from fastapi import FastAPI

from gu_ml.api.routes.router import api_router
from gu_ml.core.event_handlers import start_app_handler, stop_app_handler


def get_app() -> FastAPI:
    fast_app = FastAPI(title="gu-ml", version="v1", debug=True)
    fast_app.include_router(api_router, prefix="/gu-ml")

    fast_app.add_event_handler("startup", start_app_handler(fast_app))
    fast_app.add_event_handler("shutdown", stop_app_handler(fast_app))

    return fast_app


app = get_app()
