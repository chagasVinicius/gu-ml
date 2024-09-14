from fastapi import APIRouter
from starlette.requests import Request

from gu_ml.models.card import Card
from gu_ml.services.card_db import CardDB
import random

router = APIRouter()


@router.post("/card", response_model=Card, name="card")
def add_card(
    request: Request,
    card_data: Card,
) -> Card:
    ## prediction step
    predict = random.choice(["early", "late"])
    ## update db
    card_updated = card_data.model_copy(update={"strategy": predict})
    CardDB().insert_card(card_updated)
    return card_updated
