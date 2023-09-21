import random

# return a list containing n random ints in range 1 to 100
def random_list(n):
    # _ --> placeholder variable, signifies that value is generated but not stored or used within comprehension.
    return [random.randint(1, 100) for _ in range(n)]


# return the average of all values in the list lst
def average(lst):
    if not lst:
        return 0
    return round(sum(lst) / len(lst))


# return new list containing only odd integers
def only_odd(lst):
    return [x for x in lst if x % 2 != 0]


# return a comma-separated string representation of the elements in lst
def to_string(lst):

    
# return true if a directly followed by b
def contains(lst, a, b):

    
# return true if the lst contains duplicates
def has_duplicates(lst):
    
