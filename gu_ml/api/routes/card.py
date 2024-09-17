from fastapi import APIRouter, HTTPException
from starlette.requests import Request

from gu_ml.models.card import Card
from gu_ml.services.card_db import CardDB

from gu_ml.services.models import CardStrategyClassification
from loguru import logger

router = APIRouter()


@router.post("/card")
def add_card(
    request: Request,
    card_data: Card,
) -> Card:
    model: CardStrategyClassification = request.app.state.model
    card_updated: Card = model.predict(card_data)
    if old_card := CardDB().get_card(card_data.id):
        CardDB().update_card(card_updated)
    else:
        CardDB().insert_card(card_updated)
    return card_updated


@router.get("/card/{card_id}")
def get_card(card_id: int) -> Card:
    if card := CardDB().get_card(card_id):
        return card
    raise HTTPException(status_code=404, detail="Card not found")
