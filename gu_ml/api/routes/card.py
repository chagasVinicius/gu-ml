from fastapi import APIRouter
from starlette.requests import Request

from gu_ml.models.card import Card
from gu_ml.services.card_db import CardDB

from gu_ml.services.models import CardStrategyClassification
from loguru import logger

router = APIRouter()


@router.post("/card", response_model=Card, name="card")
def add_card(
    request: Request,
    card_data: Card,
) -> Card:
    model: CardStrategyClassification = request.app.state.model
    card_updated: Card = model.predict(card_data)
    CardDB().insert_card(card_updated)
    return card_updated


@router.get("/card/{card_id}", response_model=Card)
def get_card(card_id: int):
    card: Card = CardDB().get_card(card_id)
    return card
