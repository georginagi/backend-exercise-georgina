from _decimal import Decimal

from expects import *
from mamba import *

from actions.checkout import Checkout
from models.item import Item
from models.pricing_rules import PricingRules, VoucherRule, TShirtRule

with description('Checkout'):
    with it('calculates the total amount considering only the one product scanned'):
        item = Item('VOUCHER', 'Gift Card', Decimal(5.00))

        checkout = Checkout(PricingRules({}))
        checkout.scan(item)

        expect(checkout.calculate_total()).to(equal(item.price))

    with it('calculates correct total amount when pricing rules do not exist'):
        voucher = Item('VOUCHER', 'Gift Card', Decimal(5.00))
        t_shirt = Item('TSHIRT', 'Summer T-Shirt', Decimal(20.00))
        pants = Item('PANTS', 'Summer Pants', Decimal(7.50))

        checkout = Checkout(PricingRules({}))

        checkout.scan(voucher)
        checkout.scan(t_shirt)
        checkout.scan(pants)

        expect(checkout.calculate_total()).to(equal(Decimal(32.50)))

    with it('calculates correct total amount when pricing rules do not apply'):
        voucher = Item('VOUCHER', 'Gift Card', 5.00)
        t_shirt = Item('TSHIRT', 'Summer T-Shirt	', 20.00)
        pants = Item('PANTS', 'Summer Pants', 7.50)

        checkout = Checkout(PricingRules({'VOUCHER': VoucherRule()}))

        checkout.scan(voucher)
        checkout.scan(t_shirt)
        checkout.scan(pants)

        expect(checkout.calculate_total()).to(equal(Decimal(32.50)))

    with it('applies 2-1 when two gift cards are purchased'):
        voucher = Item('VOUCHER', 'Gift Card', 5.00)

        checkout = Checkout(PricingRules({'VOUCHER': VoucherRule()}))
        checkout.scan(voucher)
        checkout.scan(voucher)

        expect(checkout.calculate_total()).to(equal(Decimal(5.00)))

    with it('applies 2-1  only for the 2n gifts cards when 2n+1 gift cards are purchased'):
        voucher = Item('VOUCHER', 'Gift Card', 5.00)

        checkout = Checkout(PricingRules({'VOUCHER': VoucherRule()}))

        checkout.scan(voucher)
        checkout.scan(voucher)
        checkout.scan(voucher)

        expect(checkout.calculate_total()).to(equal(Decimal(10.00)))

    with it('applies pricing rule when two gift cards and one random item are purchased'):
        voucher = Item('VOUCHER', 'Gift Card', 5.00)
        t_shirt = Item('TSHIRT', 'Summer T-Shirt', 20.00)

        checkout = Checkout(PricingRules({'VOUCHER': VoucherRule()}))

        checkout.scan(voucher)
        checkout.scan(t_shirt)
        checkout.scan(voucher)

        expect(checkout.calculate_total()).to(equal(Decimal(25.00)))

    with it('applies pricing rule when three shirts are purchased'):
        t_shirt = Item('TSHIRT', 'Summer T-Shirt', 20.00)

        checkout = Checkout(PricingRules({'TSHIRT': TShirtRule()}))

        checkout.scan(t_shirt)
        checkout.scan(t_shirt)
        checkout.scan(t_shirt)

        expect(checkout.calculate_total()).to(equal(Decimal(57.00)))

    with it('applies pricing rule when at least three shirts and a random item are purchased'):
        t_shirt = Item('TSHIRT', 'Summer T-Shirt', 20.00)
        voucher = Item('VOUCHER', 'Gift Card', 5.00)

        pricing_rules_dict = {'VOUCHER': VoucherRule(), 'TSHIRT': TShirtRule()}
        pricing_rules = PricingRules(pricing_rules_dict)

        checkout = Checkout(pricing_rules)

        checkout.scan(t_shirt)
        checkout.scan(t_shirt)
        checkout.scan(t_shirt)
        checkout.scan(voucher)
        checkout.scan(t_shirt)

        expect(checkout.calculate_total()).to(equal(Decimal(81.00)))

    with it('applies pricing rules when the user purchases at least three gift cards and at least three shirts'):
        t_shirt = Item('TSHIRT', 'Summer T-Shirt', 20.00)
        voucher = Item('VOUCHER', 'Gift Card', 5.00)
        pants = Item('PANTS', 'Summer Pants', 7.50)

        pricing_rules_dict = {'VOUCHER': VoucherRule(), 'TSHIRT': TShirtRule()}

        checkout = Checkout(PricingRules(pricing_rules_dict))

        checkout.scan(voucher)
        checkout.scan(t_shirt)
        checkout.scan(voucher)
        checkout.scan(voucher)
        checkout.scan(pants)
        checkout.scan(t_shirt)
        checkout.scan(t_shirt)

        expect(checkout.calculate_total()).to(equal(Decimal(74.50)))
