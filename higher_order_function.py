

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

