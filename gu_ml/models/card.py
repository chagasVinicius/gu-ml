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
