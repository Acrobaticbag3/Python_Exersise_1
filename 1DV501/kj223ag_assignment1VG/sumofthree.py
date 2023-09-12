# assignment 7 vg task
three_Didgit = input("Provide a three digit number: ")

# try to run code
try:
    if len(three_Didgit) == 3:  # if its a three length number then we can assume that its positive # noqa: E501
        num_01, num_02, num_03 = int(three_Didgit[0]), int(three_Didgit[1]), int(three_Didgit[2])   # get and convert numbers from string to int # noqa: E501
        sum = num_01 + num_02 + num_03
        print("Sum of the three numbers is:", sum)
    elif len(three_Didgit) == 4 and three_Didgit[0] == '-':  # if it has 4 length then we check if the first string character is - aka negative # noqa: E501
        num_01, num_02, num_03 = int(three_Didgit[1]), int(three_Didgit[2]), int(three_Didgit[3])   # get and convert numbers from string to int # noqa: E501
        sum = num_02 + num_03 - num_01  # e.g: -746 -> -7 + 4 + 6 = 3
        print("Sum of the three numbers is:", sum)
    else:
        print("Invalid input.")
# chatch potential error
except ValueError:
    print("Exception occurred!")
