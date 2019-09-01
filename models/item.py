from decimal import Decimal
from dataclasses import dataclass


@dataclass
class Item:
    code: str
    name: str
    price: Decimal
