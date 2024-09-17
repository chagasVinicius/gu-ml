import pytest

# from gu_ml.core import config
from gu_ml.models.card import Card
from gu_ml.services.models import CardStrategyClassification


def test_prediction(test_client) -> None:
    card = Card.model_validate(
        {
            "id": 306,
            "name": "Blood Rage",
            "mana": 2,
            "attack": 0,
            "health": 0,
            "type": "spell",
            "god": "war",
        }
    )
    card_updated = CardStrategyClassification("./model/lgb_model.joblib").predict(card)

    assert "strategy" in card_updated.model_dump()
