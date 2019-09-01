from decimal import Decimal
from dataclasses import dataclass

from models.item import Item


@dataclass
class ScannedItem:
    item: Item
    total_price: Decimal = 0
    quantity: int = 0
