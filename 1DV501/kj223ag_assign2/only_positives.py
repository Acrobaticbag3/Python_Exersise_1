# assignment 15
# Initialize an empty list to store positive integers
positive_numbers = []
count = 0

print("Enter positive integers. End by giving a negative integer.")

# Read positive integers from the user until a negative integer is encountered
while True:
    try:
        count += 1
        integer = int(input(f"Input {count}: "))

        if integer < 0:
            break

        positive_numbers.append(integer)

    except ValueError:
        print("Invalid input. Please enter a positive or negative integer.")

# Print the count and the list of positive integers
print(f"Number of positive integers: {len(positive_numbers)}")
print(f"Positive numbers: {positive_numbers}")
