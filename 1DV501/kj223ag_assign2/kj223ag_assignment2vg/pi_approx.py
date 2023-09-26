# assignment 14
import random
import math


# employ Monte Calro method
def estimate_pi(num_points):
    inside_circle = 0

    # use '_' since value is ignored
    for _ in range(num_points):
        x = random.uniform(-1, 1)   # Generate random x value
        y = random.uniform(-1, 1)   # Generate random y value

        distance = x**2 + y**2  # calculate square of distance (0, 0)) - (x, y)

        if distance <= 1:
            inside_circle += 1

    # calculates the approximation of π
    pi_approx = 4 * inside_circle / num_points
    return pi_approx


# define actual value
pi_actual = math.pi

# compute pi approximation for different values of N
for N in [100, 10000, 1000000]:
    pi_approx = estimate_pi(N)
    error = abs(pi_actual - pi_approx)
    print(f"Approximation for N = {N}: {pi_approx}, Error: {error}")
