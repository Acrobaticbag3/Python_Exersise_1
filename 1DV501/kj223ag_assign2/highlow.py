# assignment 4
import random


# logic for the guesses
def Check_Guess(rand, guess):
    if rand > guess:
        print("Higher:")
    elif rand < guess:
        print("Lower:")
    elif rand == guess:
        print(f"Congrats, you found my number {rand}, amount of times guessed: ", end="")  # noqa: E501


# start of main
rand = random.randint(1, 100)
guesses = 0
guess = -1

# run for as long as our guess != the computers number.
while guess != rand and guesses != 10:
    guesses += 1
    try:
        guess = int(input(f"Guess {guesses} : "))
        Check_Guess(rand, guess)
    except ValueError:
        print("Provide an integer...")

if guesses <= 3:
    print(guesses, "- Excellent!")
elif 4 < guesses < 8:
    print(guesses, "- Satisfactory")
else:
    print(guesses, "- Too many guesses, cant exede 10")
