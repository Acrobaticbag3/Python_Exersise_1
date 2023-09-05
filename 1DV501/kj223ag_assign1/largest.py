# assignment 10
a = int(input("Please provide three integers A, B, C. \n Enter A:"))
b = int(input("Enter B:"))
c = int(input("Enter C:"))

largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

print("The largest number is:", largest)