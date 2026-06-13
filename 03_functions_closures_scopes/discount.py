# Build a function that creates discount calculators.
# Each returned function should permanently remember its own discount rate.


def discount(disc):
    def price(p):
        return p-(p*disc/100)
    return price

final_price = discount(20)
print(final_price(200))