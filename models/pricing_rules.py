from dataclasses import dataclass
from _decimal import Decimal


@dataclass
class PricingRules:
    rules: dict


class PricingRule:
    def apply_rule(self):
        raise ValueError


class VoucherRule(PricingRule):
    def apply_rule(self, scanned_item):
        if scanned_item.quantity % 2 == 0:
            total_price = Decimal(scanned_item.item.price) * Decimal(scanned_item.quantity / 2)
        else:
            total_price = Decimal(scanned_item.item.price) * Decimal((scanned_item.quantity // 2)) + \
                               Decimal(scanned_item.item.price)
        return total_price


class TShirtRule(PricingRule):
    def apply_rule(self, scanned_item):
        if scanned_item.quantity >= 3:
            total_price = Decimal(scanned_item.item.price * 0.95) * Decimal(scanned_item.quantity)
        else:
            total_price = Decimal(scanned_item.item.price * self.quantity)
        return total_price
