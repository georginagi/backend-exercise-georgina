from _decimal import Decimal

from expects import *
from mamba import *

from actions.checkout import Checkout
from models.item import Item
from models.pricing_rules import PricingRules

with description('Checkout'):
    with it('calculates the total amount considering only the one product scanned'):
        item = Item('VOUCHER', 'Gift Card', Decimal(5.00))

        checkout = Checkout(PricingRules())
        checkout.scan(item)

        expect(checkout.calculate_total()).to(equal(item.price))
