import random


# iterate through elements in input, count occurrences of unique number in list
def count_occurrences(lst):
    occurrence_dict = {}     # initializ an empty dictionary
    for num in lst:
        if num in occurrence_dict:
            occurrence_dict[num] += 1   # increase count if doup is found
        else:
            occurrence_dict[num] = 1    # start count if unique is found

    # sort keys (numbers) in ascending order
    sorted_dict = dict(sorted(occurrence_dict.items()))
    return sorted_dict


# generate our random lst
lst = [random.randint(1, 10) for _ in range(100)]
result = count_occurrences(lst)

# iterate through our posibileties
for i in range(1, 11):
    # retrieve the count of each number, default to 0.
    print(f"{i}\t{result.get(i, 0)}")
