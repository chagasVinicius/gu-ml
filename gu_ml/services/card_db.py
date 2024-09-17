from typing import Dict, List
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

    def _update_card(self, card: Card):
        with self.db as db:
            db.cursor.execute(
                """
                UPDATE cards
                SET name=%(name)s, mana=%(mana)s, attack=%(attack)s, health=%(health)s, type=%(type)s, god=%(god)s, strategy=%(strategy)s
                WHERE id = %(id)s
                """,
                card.model_dump(),
            )
            db.connection.commit()

    def update_card(self, card: Card) -> Card:
        try:
            self._update_card(card)
            return card
        except Exception as e:
            logger.info(f"Failed to update card:\n{e}")
            raise e

    def _get_card(self, card_id: int) -> Dict | None:
        with self.db as db:
            try:
                return db.cursor.execute(
                    """
                SELECT * FROM cards WHERE id = %s
                """,
                    (card_id,),
                ).fetchone()
            except Exception as e:
                logger.warning(e)
                pass

    def get_card(self, card_id: int) -> Dict:
        try:
            logger.info(self._get_card(card_id))
            return self._get_card(card_id)
        except Exception as e:
            logger.info(f"Failed to retrieve a card:\n{e}")
            raise e
