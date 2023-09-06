# assignment 7 vg task
three_Didgit = input("Provide a three digit number: ")

# Try to run code Note: - Does not work with negative numbers
try:
    num_01, num_02, num_03 = int(three_Didgit[0]), int(three_Didgit[1]), int(three_Didgit[2])   # get and convert numbers from string to int
    sum = num_01 + num_02 + num_03
    print("Sum of the three numbers is:",sum)
# chatch potential error
except:
    print("Exeption occured!")