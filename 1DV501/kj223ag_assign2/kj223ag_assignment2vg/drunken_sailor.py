# assignment 21

import random


# simulate drunken sailors walking on a grid
def simulate_drunken_sailors(size, max_steps, num_sailors):
    sailors_in_water = 0

    # iterate through each sailor
    for _ in range(num_sailors):
        # start pos for sailor
        x, y = 0, 0

        # simulate the sailor's steps
        for _ in range(max_steps):  # use '_' since value is ignored
            step = random.choice(["up", "down", "left", "right"])

            # update the sailor's position based on the random step
            if step == "up":
                y += 1
            elif step == "down":
                y -= 1
            elif step == "left":
                x -= 1
            elif step == "right":
                x += 1

            # check is the sailor still in our grid
            if abs(x) > size or abs(y) > size:
                sailors_in_water += 1
                break

    return sailors_in_water


# user input for the size of the grid, number of steps, and number of sailors
size = int(input("Enter the size: "))
max_steps = int(input("Enter the number of steps: "))
num_sailors = int(input("Enter the number of sailors: "))

# simulate sailors movements
sailors_in_water = simulate_drunken_sailors(size, max_steps, num_sailors)

# calculate the percentage of sailors who fell into the water
percentage_in_water = (sailors_in_water / num_sailors) * 100

# print the results, including the count and percentage of sailors in the water
print(f"Out of {num_sailors} drunk sailors, {sailors_in_water} ({percentage_in_water:.2f}%) fell into the water.")
