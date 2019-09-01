from _decimal import Decimal

from models.item import Item
from models.pricing_rules import PricingRules
from models.scanned_item import ScannedItem


class Checkout:

    def __init__(self, pricing_rules: PricingRules):
        self.pricing_rules = pricing_rules
        self.scanned_items_dict = {}

    def scan(self, item: Item):
        if item.name not in self.scanned_items_dict:
            self.scanned_items_dict.update({item.name: ScannedItem(item=item, total_price=item.price, quantity=1)})
        else:
            self.scanned_items_dict[item.name].quantity += 1

    def calculate_total(self):
        amount = 0
        for scanned_item in self.scanned_items_dict.values():
            if len(self.pricing_rules.rules) == 0:
                scanned_item.total_price = scanned_item.total_price * scanned_item.quantity
            else:
                if scanned_item.item.code in self.pricing_rules.rules:
                    rule = self.pricing_rules.rules[scanned_item.item.code]
                    scanned_item.total_price = rule.apply_rule(scanned_item)
                else:
                    scanned_item.total_price = scanned_item.total_price * scanned_item.quantity
            amount += Decimal(scanned_item.total_price)
        return amount
