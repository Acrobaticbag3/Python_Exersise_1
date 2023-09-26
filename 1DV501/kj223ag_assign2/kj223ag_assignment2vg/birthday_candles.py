# Constants
MAX_AGE = 100  # maximum age
CANDLES_PER_BOX = 24  # amount of candles per box

# Initialize variables
total_boxes = 0
remaining_candles = 0

# Iterate through each year
for current_age in range(1, MAX_AGE + 1):
    # Check if we need to buy more boxes
    while remaining_candles < current_age:
        remaining_candles += CANDLES_PER_BOX
        total_boxes += 1

    # Print only if we need to buy boxes
    if remaining_candles >= current_age:
        print(f"Before birthday {current_age}, buy {total_boxes} box(es)")

# Print the total number of boxes and remaining candles
print(f"Total number of boxes: {total_boxes}, Remaining candles: {remaining_candles}")
