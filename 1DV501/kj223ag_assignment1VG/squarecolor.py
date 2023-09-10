# assignment 15 vg task
# define the function to determine the square's color
def get_square_color(letter, number):
    if letter in 'aceg' and number % 2 == 1:    # all odd squares on aceg are black 
        return "Black"
    elif letter in 'bdfh' and number % 2 == 0:  # all even squeres on bdfh are black
        return "Black"
    else:                   # the rest are white
        return "White"

# get the square identifier from the user
square_identifier = input("Enter a chess square identifier (e.g. e5): ")

# ensure that the input is in the correct format (letter+number, e.g., e5) and exists on the board
if len(square_identifier) != 2 or not square_identifier[0] in 'abcdefgh' or not square_identifier[1] in '12345678':
    print("Invalid input. Please enter a valid square identifier (e.g., e5).")
else:
    letter, number = square_identifier[0], int(square_identifier[1])
    
    # determine and print the square's color
    square_color = get_square_color(letter, number)
    print(f"{square_identifier} is {square_color}")