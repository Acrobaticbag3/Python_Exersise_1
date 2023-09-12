# assignment 2
n = int(input("Enter a positive integer: "))
if n < 0:
    print("Must be a positive number!")

for i in range(n):
    if i % 2 == 1:
        print("Odd numbers using for: ", i, end=' ')
    i = i + 1

    while i < n:
        if i % 2 == 1:
            print("Odd numbers using while: ", i, end=' ')
        i = i + 1
