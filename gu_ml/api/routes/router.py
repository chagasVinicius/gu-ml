from fastapi import APIRouter

from gu_ml.api.routes import healthcheck

api_router = APIRouter()
api_router.include_router(healthcheck.router, tags=["health"], prefix="")
