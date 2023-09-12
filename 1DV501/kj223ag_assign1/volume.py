# Assignment 5
import math

r = int(input("Provide a radius: "))
r = r ** 3

v = 4/3 * math.pi
v = v * r

print("The volume is:", round(v, 1))
