from fastapi import APIRouter

from gu_ml.models.healthcheck import HealthCheck


router = APIRouter()


@router.get("/healthcheck", response_model=HealthCheck, name="healthcheck")
def healthcheck() -> HealthCheck:
    return HealthCheck(health=True)
