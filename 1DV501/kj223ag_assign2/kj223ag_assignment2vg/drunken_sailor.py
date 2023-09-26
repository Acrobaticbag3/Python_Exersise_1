import random


def simulate_drunken_sailors(size, max_steps, num_sailors):
    sailors_in_water = 0

    for _ in range(num_sailors):
        x, y = 0, 0
        for _ in range(max_steps):
            # Generate a random step (up, down, left, or right)
            step = random.choice(["up", "down", "left", "right"])

            if step == "up":
                y += 1
            elif step == "down":
                y -= 1
            elif step == "left":
                x -= 1
            elif step == "right":
                x += 1

            # Check if the sailor is in the water (outside the boundary)
            if abs(x) > size or abs(y) > size:
                sailors_in_water += 1
                break

    return sailors_in_water


size = int(input("Enter the size: "))
max_steps = int(input("Enter the number of steps: "))
num_sailors = int(input("Enter the number of sailors: "))

sailors_in_water = simulate_drunken_sailors(size, max_steps, num_sailors)

percentage_in_water = (sailors_in_water / num_sailors) * 100
print(f"Out of {num_sailors} drunk sailors, {sailors_in_water} ({percentage_in_water:.2f}%) fell into the water.")
