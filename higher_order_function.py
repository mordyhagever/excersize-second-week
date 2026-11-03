

#tar1

def double(n):
    return n * 2
def rounded(n):
    round(n, 2)
square = lambda n: n * n

def apply_to_all(numbers, action):
    new_list = []
    for num in numbers:
        new_list.append(action(num))
    return new_list

# print(apply_to_all([1, 2, 3], double))
# print(apply_to_all([1, 2, 3], lambda n: n * n))
# print(apply_to_all([1.6, 2.4], round))


#tar2
prices = [20, 75, 120, 45, 90]

filtered = list(filter(lambda p: p > 50, prices))
add_ten = list(map(lambda p: p + 10, filtered))

# print(filtered)
# print(add_ten)


#tar3
words = ["banana", "fig", "cherry", "kiwi"]
students = [("Dana", 92), ("Avi", 78), ("Noa", 85)]

# print(sorted(words, key=len))
# print(max(words, key=len))
# sorted_students = sorted(students, key=lambda p: p[1])
# for student in sorted_students:
#     print(student[0])


#tar4

def make_discount(percent):
    def calc(price):
        return price - price * (percent / 100)
    return calc

ten_off = make_discount(10)
half_price = make_discount(50)

# print(ten_off(200))
# print(half_price(200))

