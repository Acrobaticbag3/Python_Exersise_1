# assignment 8 VG

# function that decides whether an int is even, odd, or 0
def check_input(i, odd, even, zeros):
    # logic that checks if an int is even, odd, or 0
    if i % 2 == 0 and i != 0:
        even += 1
    elif i % 2 == 1 and i != 0:
        odd += 1
    else:
        zeros += 1

    return even, odd, zeros


# Main program
# initialize useful variables
odd = 0
even = 0
zeros = 0

try:
    # input, convert to list
    n = list(input("Enter a large positive integer: "))

    for i in range(len(n)):
        i = int(n[i])
        # get, store values
        even, odd, zeros = check_input(i, odd, even, zeros)

    # print the results
    print(f"Zeros: {zeros} \nOdd: {odd} \nEven: {even}", end='')

# catch potential ValueError, e.g., non-integer or a string input
except ValueError:
    print("Error, expected a positive integer.")
