

#tar1

def make_greeting(name, greeting = "Hello", punct = "!"):
    return f"{greeting}, {name}{punct}"

# print(make_greeting("Dana"))
# print(make_greeting("Avi", "Good morning"))
# print(make_greeting("Noa", punct="?"))

#tar2

def average(*numbers):
    subtotal = sum(numbers)
    if subtotal == 0:
        raise ValueError("error: need at least one number")
    return subtotal / len(numbers)
# print(average(80, 90))
# print(average(70, 80, 90, 100))
# try:
#     average()
# except ValueError as e:
#     print("error", e)



