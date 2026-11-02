#tar1

def to_number(text):
    try:
        return int(text)
    except ValueError:
        return f"{text} is not a number"
# print(to_number("42"))
# print(to_number("hello"))
# print(to_number("7"))

#tar2

def safe_divide(text1, text2):
    try:
        result = int(text1) / int(text2)
        return result
    except ValueError:
        return "numbers only"
    except ZeroDivisionError:
        return "cannot divide by zero"
# print(safe_divide("10", "4"))
# print(safe_divide("10", "0"))
# print(safe_divide("ten", "2"))

#tar3

# try:
#     number = int("12ac")
# except ValueError as e:
#     print(f"Could not convert: {e}")
#


#tar4

def pick(names, position_text):
    try:
        return names[int(position_text) - 1]
    except IndexError:
        return "no such position"
    except ValueError:
        return "not a number"
arr = ["Dana", "Avi", "Noa"]
# print(pick(arr, "2"))
# print(pick(arr, "abc"))
# print(pick(arr, "9"))

#tar5
def read_age(text):
    try:
        if int(text) < 0:
            raise ValueError("Number cannot be negative")
        return int(text)

    except ValueError as e:
        return e
#print(read_age("sd"))

