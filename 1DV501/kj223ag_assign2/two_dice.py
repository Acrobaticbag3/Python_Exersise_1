# assignment 16
from random import randint  # Only import randint from random

dice_amount = [0] * 11  # initealize set on 0, add 13 (1-12) elements

ROLLS = 10000
for i in range(ROLLS):
    roll_check = randint(2, 12)     # create rand int
    dice_amount[roll_check - 2] += 1    # check rand int matced element, add +1 to the "size"

print(f"Frequency table (sum,count) for rolling two dices {ROLLS} times:")
for i in range(2, 13):
    print(f"{i}: {dice_amount[i - 2]}")
