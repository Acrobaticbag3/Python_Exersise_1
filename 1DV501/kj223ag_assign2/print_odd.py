# assignment 2
def For_Loop(n):    # For loop part of the task
    print("Loop using for:", end=' ')

    for i in range(1, n, 2):
        print(i, end=' ')
    print("\n")


def While_Loop(n):  # While loop part of the task
    print("Loop using while:", end=' ')

    i = 0
    while i < n:
        i += 1

        if i % 2 == 1:
            print(i, end=' ')

    print("\n")


# Start of Main
try:    # Try to get input from user
    n = int(input("Please provide a positive integer: "))

except ValueError:  # Catch wrongfull input
    print("Value error: Please enter a valid integer.")

else:
    if isinstance(n, int):  # is n an int?
        if n > 0:
            For_Loop(n)
            While_Loop(n)
        elif n < 0:
            print(f"{n} is negative. Please provide a positive number.")
    else:
        print(f"Wrong format, expected integer not {type(n)}")
