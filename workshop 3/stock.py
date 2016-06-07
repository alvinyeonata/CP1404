"""
import random

__author__ = 'Lindsay Ward'
MAX_INCREASE = 0.175
MAX_DECREASE = 0.05
MIN_PRICE = 1
MAX_PRICE = 100
INITIAL_PRICE = 10.0
day = 0
price = INITIAL_PRICE
print("Starting price is: ${:,.2f}".format(price))


while price >= MIN_PRICE and price <= MAX_PRICE:
    priceChange = 0

    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        priceChange = random.uniform(0, MAX_INCREASE)
        day= day + 1
    else:
        # generate a random floating-point number
        # between negative MAX_INCREASE and 0
        priceChange = random.uniform(-MAX_DECREASE, 0)
        day= day + 1

    price *= (1 + priceChange)
    print("On day",day,"price is: ${:,.2f}".format(price))

"""

import random

__author__ = 'Lindsay Ward'
MAX_INCREASE = 0.175
MAX_DECREASE = 0.05
MIN_PRICE = 1
MAX_PRICE = 100
INITIAL_PRICE = 10.0
day = 0
price = INITIAL_PRICE

def format_currency(price):
    currency ="Starting price is: ${:,.2f}".format(price)
    return currency


print("Starting price is: {}".format(format_currency(price)))
while price >= MIN_PRICE and price <= MAX_PRICE:
    priceChange = 0

    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        priceChange = random.uniform(0, MAX_INCREASE)
        day= day + 1
    else:
        # generate a random floating-point number
        # between negative MAX_INCREASE and 0
        priceChange = random.uniform(-MAX_DECREASE, 0)
        day= day + 1

    price *= (1 + priceChange)
    print("on day {} price is {}".format(day,format_currency(price)))


