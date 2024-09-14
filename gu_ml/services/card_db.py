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
            raise e
