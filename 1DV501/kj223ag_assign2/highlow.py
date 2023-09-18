# assignment 4
import random


# Logic for the guesses
def Check_Guess(rand, guess):
    if rand > guess:
        print("Higher:")
    elif rand < guess:
        print("Lower:")
    elif rand == guess:
        print(f"Congrats, you found my number {rand}, amount of times guessed: ", end="")  # noqa: E501


# Start of main
rand = random.randint(1, 100)
guesses = 0
guess = -1

# Run for as long as our guess != the computers number.
while guess != rand:
    guesses += 1
    try:
        guess = int(input(f"Guess {guesses} : "))
        Check_Guess(rand, guess)
    except ValueError:
        print("Provide an intager...")

print(guesses, "- Excellent!")
