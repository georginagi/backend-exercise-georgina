## Backend Exercise

Nextail is thinking about expanding its business and not only forecast sales in the stores but also manage the cash register. 

The first store where we will introduce our software will sell the following 3 products.

| CODE    | NAME           | PRICE  |
|---------|----------------|--------|
| VOUCHER | Gift Card      | 5.00€  |
| TSHIRT  | Summer T-Shirt | 20.00€ |
| PANTS   | Summer Pants   | 7.50€  |

The different departments have agreed the following discounts:

● A 2-for-1 special on VOUCHER items.

● If you buy 3 or more TSHIRT items, the price per unit should be 19.00€.

● Items can be scanned in any order, and the cashier should return the total amount to be
paid.

The interface for the checkout process has the following specifications:

● The Checkout constructor receives a pricing_rules object

● The Checkout object has a scan method that receives one item at a time


## Examples:

● Items: VOUCHER, TSHIRT, PANTS - Total: 32.50€

● Items: VOUCHER, TSHIRT, VOUCHER - Total: 25.00€

● Items: TSHIRT, TSHIRT, TSHIRT, VOUCHER, TSHIRT - Total: 81.00€

● Items: VOUCHER, TSHIRT, VOUCHER, VOUCHER, PANTS, TSHIRT, TSHIRT - Total:
74.50€

## Requirements

docker==latest

python==3.7.4
pip>=19.2.2
mamba==0.10.0
expects==0.9.0


## How to run the tests

There are two ways to run the tests for this project:

- If you have docker installed in your machine, execute:

``` make test ```

- otherwise you will be needing Python 3.7 and pip to execute the following:


``` pip install -r requirements.txt ``` 

``` ./scripts/runners/test_unit.sh ```

If none of this applies, have a look at:
install docker: https://docs.docker.com/install/
install Python and pip: https://www.python.org/downloads/

## Implementation

- This exercise challenged me somehow on how I view the Item as an entity and which entity is responsible
for the pricing rule application. Since the pricing rules are given in the Checkout constructor I decided that the Item model 
is unaware of whether it has any pricing rules that go with it and left it with its basic attributes.

- Regarding the pricing rules, initially, I wanted to create an abstract pricing rule model and perhaps that might have been
the goal but I couldn't find a proper way to describe both rules in an abstract matter.
For that reason and since we have only two pricing rules I hard coded their logic. I believe
that given a scenario with more pricing rules we would have enough similar patterns to create
a better abstraction.

- Regarding the tests, I realised after completing that the tests for the checkout were not only
testing the checkout unit but also whether the hard coded logic of the rule was applied correctly.
For that reason, I would prefer to have written tests for the rules themselves when implementing them
and not only receive feedback for their validity from the checkout spec.
