

#tar2

def add_price(price, added_price):
    new_total = price
    new_total += added_price
    return new_total
# print(add_price(30))
# print(total)
# total = 0
# total = add_price(total, 10)
# total = add_price(total, 10)
# print(total)
#
# print(add_price(0, 10))
# print(add_price(0, 10))



#tar3

TAX = 1.17
def apply_tax(prices):
    new_prices = []
    for i in range(len(prices)):
        new_prices.append(prices[i] * TAX)
    return new_prices

# prices = [100, 50]
# with_tax = apply_tax(prices)
# print(prices)
# print(with_tax)


#tar4

def calculate_total(prices):
    total = 0
    for price in prices:
        total += price
    return total

def show_total(prices):
    print(f"Total: {calculate_total(prices)}")

#show_total([10, 20, 30])


#tar5

def top_three(numbers):
    copy = numbers
    big_to_small = []
    copy = sorted(copy)
    for i in range(3):
        big_to_small.append(copy[-1])
        copy.pop(-1)
    return big_to_small

scores = [70, 95, 88, 60, 99]
# print(top_three(scores))
# print(scores)



