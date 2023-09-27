# assignment 2

# For loop part of the task
def For_Loop(n):
    print("Loop using for:", end=' ')

    for i in range(1, n+1, 2):
        print(i, end=' ')
    print("\n")


# While loop part of the task
def While_Loop(n):
    print("Loop using while:", end=' ')

    i = 0
    while i < n:
        i += 1

        if i % 2 == 1:
            print(i, end=' ')

    print("\n")


# Start of Main
try:    # try to get input from user
    n = int(input("Please provide a positive integer: "))

# catch wrongfull input
except ValueError:
    print("Value error: Please enter a valid integer.")


else:
    if n > 0:
        For_Loop(n)
        While_Loop(n)
    elif n < 0:
        print(f"{n} is negative. Please provide a positive number.")
