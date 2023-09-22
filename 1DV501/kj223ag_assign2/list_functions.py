import random


# return a list containing n random ints in range 1 to 100
def random_list(n):
    """""
    _ --> placeholder variable, signifies that value is generated but not
    stored or used within comprehension.
    """""
    print([random.randint(1, 100) for _ in range(n)])


# return the average of all values in the list lst
def average(lst):
    sum = 0

    for i in range(len(lst)):
        sum += lst[i]

    new_sum = sum / len(lst)
    print(f"{new_sum:.0f}")


# return new list containing only odd integers
def only_odd(lst):
    print([x for x in lst if x % 2 != 0])


# return a comma-separated string representation of the elements in lst
def to_string(lst):
    lst = str(lst)
    print(f'"{lst}"')


# return true if a directly followed by b
def contains(lst, a, b):
    n = a+1

    if n == b:
        print(f"{True}")
    else:
        print(f"{False}")


# return true if the lst contains duplicates
def is_duplicate(lst):
    if len(lst) != len(set(lst)):
        print("List has duplicates")
    else:
        print("List has no duplicates")
