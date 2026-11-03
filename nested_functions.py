

#tar1

def format_receipt(items):
    def line(name, price):
        return name.ljust(10) + str(price)

    lines = []
    for name, price in items:
        lines.append(line(name, price))
    return "\n".join(lines)

# print(format_receipt([("Milk", 6), ("Bread", 9)]))

#tar2
def make_greeter(greeting):
    def get_name(name):
        return f"{greeting}, {name}"

    return get_name

hello = make_greeter("Hello")
shalom = make_greeter("Shalom")
# print(hello("Dana"))
# print(shalom("Avi"))


#tar4
# def make_counter(step):
#     def grow(growth):
#         return growth + step
#     return grow
# by_two = make_counter(2)
# by_ten = make_counter(10)
#
# print(by_two(), by_two())
# print(by_ten())
# print(by_two())