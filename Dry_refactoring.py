


#tar1

def get_items(name, amount, price):
    arr = [name, amount, price]
    return arr

def print_receipt(name, amount, price):
    stuff = get_items(name, amount, price)
    print(f"{stuff[0]}, {stuff[1]} x {stuff[2]} = {stuff[1] * stuff[2]}")

# print_receipt("Pen", 5, 4)
# print_receipt("Notebook", 12, 2)
# print_receipt("Bag", 60, 1)
# print("Total:" , 5 * 4 + 12 * 2 + 60 * 1)

#tar2

def parity(num):
    if num % 2 == 0:
        return "even"
    return "odd"
# print(parity(4))
# print(parity(7))

#tar3

#מיותרת
#מיותרת
#מזיקה - זה לא נכון
#טובה

#tar4

def calculate_bmi(weight, height):
    return round(weight / (height * height), 1)
#print(f"BMI: {calculate_bmi(70, 1.75)}")

