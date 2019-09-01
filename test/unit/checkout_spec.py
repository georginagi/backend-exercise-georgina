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

    with it('calculates correct total amount when pricing rules do not exist'):
        voucher = Item('VOUCHER', 'Gift Card', Decimal(5.00))
        t_shirt = Item('TSHIRT', 'Summer T-Shirt', Decimal(20.00))
        pants = Item('PANTS', 'Summer Pants', Decimal(7.50))

        checkout = Checkout(PricingRules())

        checkout.scan(voucher)
        checkout.scan(t_shirt)
        checkout.scan(pants)

        expect(checkout.calculate_total()).to(equal(Decimal(32.50)))