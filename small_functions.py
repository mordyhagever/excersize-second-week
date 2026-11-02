#כל הקריאות לפונקציה נמצאים בהערה כדי שלא יפריעו לתרגילים אחרים


#tar1

BIG_NUM = 500
SMALL_NUM = 50
def check_multiple_size(num1, num2):
    num3 = num1 * num2
    if num3 > BIG_NUM:
        num3 -= 50
    return num3
# print(check_multiple_size(120, 5))
# print(check_multiple_size(30, 2))

#tar2

#total_price
#number_of_students
#correct
#correct
#get_average

#tar3

def calculate_average(grades):
    total = 0
    for g in grades:
        total += g
    avg = total / len(grades)
    return avg

def is_passing(avg):
    if calculate_average(avg) >= 55:
        return True
    return False

def print_report(name, avg):
    if is_passing(avg):
        print(f"{name}, average: {calculate_average(avg)} - passes")
    else:
        print(f"{name}, average: {calculate_average(avg)} - failed")

# print_report("Dana", [80, 85])
# print_report("Avi", [50, 46])


#tar4

MINIMUM_FREE_ORDER = 200
SMALL_ORDER_FEE = 30
def price_after_fee_check(total):
    if total < MINIMUM_FREE_ORDER:
        total += SMALL_ORDER_FEE
    return total
# print(price_after_fee_check(150))
# print(price_after_fee_check(250))


#tar5

def is_valid_password(password: str):
    arr = ["0123456789"]
    digit = False
    for letter in password:
        if letter in arr:
            digit = True

    if len(password) >= 8 and digit is True:
        return True
    return False





