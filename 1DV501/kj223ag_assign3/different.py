import random


# convert into a set, get uniqe elements. Convert back and return as lst
def different(lst):
    temp_st = list(set(lst))
    temp_st.sort()
    return temp_st


# generate our random input
lst = [random.randint(1, 200) for _ in range(100)]
unique_values = different(lst)
print(f"Different integers: {unique_values}")
