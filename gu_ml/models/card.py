from typing import Optional
from pydantic import BaseModel


class Card(BaseModel):
    id: int
    name: str
    mana: int
    attack: int
    health: int
    type: str
    god: str
    strategy: Optional[str] = None


class CardPreProcessed(BaseModel):
    type_categories: int
    god_categories: int
    mana_group: int
    health_group: int
    attack_group: int
