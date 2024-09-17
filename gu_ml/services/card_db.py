from typing import Dict
from loguru import logger
from gu_ml.services.database import PgDatabase
from gu_ml.models.card import Card


class CardDB:
    def __init__(self) -> None:
        self.db = PgDatabase()

    def _insert_card(self, card: Card):
        with self.db as db:
            db.cursor.execute(
                """
                INSERT INTO cards(id, name, mana, attack, health, type, god, strategy)
                VALUES (%(id)s, %(name)s, %(mana)s, %(attack)s, %(health)s, %(type)s, %(god)s, %(strategy)s);
                """,
                card.model_dump(),
            )
            db.connection.commit()

    def insert_card(self, card: Card) -> Card:
        try:
            self._insert_card(card)
            return card
        except Exception as e:
            logger.info(f"Failed to insert new card:\n{e}")
            raise e

    def _get_card(self, card_id: int) -> Dict:
        with self.db as db:
            return db.cursor.execute(
                """
                SELECT * FROM cards WHERE id = %s
                """,
                (card_id,),
            ).fetchone()

    def get_card(self, card_id: int) -> Card:
        try:
            card: Card = self._get_card(card_id)
            return card
        except Exception as e:
            logger.info(f"Failed to retrieve a card:\n{e}")
            raise e
