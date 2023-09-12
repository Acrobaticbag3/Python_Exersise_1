# assignment 1

# store usefull variables
n = 0
sum = 0

while n != 101:
    if n % 2 == 0:  # check if n is devisable by 2
        print(n)
        sum = sum + n
    n = n+1
print(sum)
