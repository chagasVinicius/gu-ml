import joblib
import numpy as np
from loguru import logger

from gu_ml.models.card import Card, CardPreProcessed


class CardStrategyClassification:
    def __init__(self, path: str) -> None:
        self.type_categories = {"creature": 0, "spell": 1, "weapon": 2, "god power": 3}
        self.god_categories = {
            "neutral": 0,
            "light": 1,
            "nature": 2,
            "deception": 3,
            "death": 4,
            "war": 5,
            "magic": 6,
        }
        self.continuous_bins = {
            "mana": np.array([-0.016, 3.2, 6.4, 9.6, 12.8, 16.0]),
            "attack": np.array([-0.013, 2.6, 5.2, 7.8, 10.4, 13.0]),
            "health": np.array([-0.017, 3.4, 6.8, 10.2, 13.6, 17.0]),
        }
        self.path = path
        self._load_local_model()

    def _load_local_model(self) -> None:
        self.model = joblib.load(self.path)

    def _get_category_by_bin(
        self, value: int, bin_type: str, category_range: int = 5
    ) -> int:
        bins = self.continuous_bins.get(bin_type)
        for cat in range(0, category_range):
            value_max = bins[: cat + 2].max()
            if value < value_max:
                return cat
        return category_range

    def _pre_process(self, card: Card) -> np.ndarray:
        logger.debug("Pre-processing payload.")
        card_dict = card.model_dump()
        god_categories = self.god_categories.get(card_dict.get("god"))
        type_categories = self.type_categories.get(card_dict.get("type"))
        mana_group = self._get_category_by_bin(card_dict.get("mana"), bin_type="mana")
        health_group = self._get_category_by_bin(
            card_dict.get("health"), bin_type="health"
        )
        attack_group = self._get_category_by_bin(
            card_dict.get("attack"), bin_type="attack"
        )
        return np.asarray(
            list(
                CardPreProcessed(
                    type_categories=type_categories,
                    god_categories=god_categories,
                    mana_group=mana_group,
                    health_group=health_group,
                    attack_group=attack_group,
                )
                .model_dump()
                .values()
            )
        ).reshape(1, -1)

    def _post_process(self, card: Card, prediction: np.ndarray) -> Card:
        logger.debug("Post-processing prediction.")
        category_label = "late" if prediction > 0.5 else "early"
        return card.model_copy(update={"strategy": category_label})

    def _predict(self, features: np.ndarray) -> np.ndarray:
        logger.debug("Predicting.")
        prediction_result = self.model.predict(features)
        return prediction_result

    def predict(self, card: Card) -> Card:
        pre_processed_payload = self._pre_process(card)
        prediction = self._predict(pre_processed_payload)
        logger.info(prediction)
        post_processed_result: Card = self._post_process(card, prediction)

        return post_processed_result
