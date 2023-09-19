import random


# Main program
def main():
    # ask user for input, check if positive
    n = int(input("Enter number of integers to be generated: "))
    if n < 0:
        print("Please enter a positive number.")
        exit()

    # initialize usefull variables
    min_val = 100
    max_val = 1
    total_val = 0

    # print 10 nums, check size differens and apply logic accordingly
    print("Generated values: ", end='')
    for i in range(1, n+1):
        rnd_num = random.randint(1, 100)
        total_val += rnd_num
        print(rnd_num, end=' ')

        if max_val < rnd_num:
            max_val = rnd_num
        elif min_val > rnd_num:
            min_val = rnd_num

    print()

    avrage = total_val / n

    print(f"Average, min, and max are {avrage:.2f}, {min_val} and {max_val}.")


# Start the program
if __name__ == "__main__":
    main()
