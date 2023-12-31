import math


# calculate our distance
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


try:
    # get user input for values
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    # calculate distance
    dist = distance(x1, y1, x2, y2)
    print(f"The distance between ({x1:.1f},{y1:.1f})"
          + f" and ({x2:.1f},{y2:.1f}) is {dist:.3f}")

except ValueError:  # catch potential value error
    print("Enter a valid integer.")
