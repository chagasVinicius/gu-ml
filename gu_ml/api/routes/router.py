from fastapi import APIRouter

from gu_ml.api.routes import healthcheck
from gu_ml.api.routes import card

api_router = APIRouter()
api_router.include_router(healthcheck.router, tags=["health"], prefix="")
api_router.include_router(card.router, tags=["card"], prefix="")
