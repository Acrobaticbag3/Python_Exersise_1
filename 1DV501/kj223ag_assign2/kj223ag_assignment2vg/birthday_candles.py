# assignment 9

# constants
AGE = 100
CANDLES_PER_BOX = 24

# initialize usefull variables
candles_left = 0
total_boxes = 0

# calculate candles needed for each birthday
for i in range(AGE + 1):
    candles_needed = i

    # do we need to buy more candles to proceed?
    if candles_needed > candles_left:
        boxes_to_buy = (candles_needed - candles_left + CANDLES_PER_BOX - 1) // CANDLES_PER_BOX
        candles_left += boxes_to_buy * CANDLES_PER_BOX - candles_needed

        # update the total number of boxes and print message
        total_boxes += boxes_to_buy
        print(f"Before birthday {i}, buy {boxes_to_buy} box(es)")

    # use up our candles
    else:
        candles_left -= candles_needed

# calculate remaining candles after the 100th birthday
remaining_boxes = candles_left // CANDLES_PER_BOX

# print total number of boxes and remaining candles
print(f"Total number of boxes: {total_boxes + remaining_boxes},"
      + f" Remaining candles: {candles_left}")
