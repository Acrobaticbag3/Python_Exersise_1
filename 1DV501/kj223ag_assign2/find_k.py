# assignment 3
def find_smallest_k(n):
    k = 1
    sum_of_odds = 1

    while sum_of_odds <= n:
        k += 2
        sum_of_odds += k

    return k


def find_largest_k(n):
    k = 0
    sum_of_evens = 0

    while sum_of_evens <= n:
        k += 2
        sum_of_evens += k

    return k - 2


# main Program
n = int(input("Enter a positive integer: "))    # Get user input

if n <= 0:  # check if n is positive
    print("Error: Please enter a positive integer.")

if isinstance(n, int):  # is n an int?
    smallest_k = find_smallest_k(n)
    largest_k = find_largest_k(n)

    print(f"{smallest_k} is the smallest k such that 1+3+5+...+k > {n}")
    print(f"{largest_k} is the largest k such that 0+2+4+6+...+k < {n}")

else:   # wrong format!
    print(f"Wrong format, expected integer not {type(n)}")
