# assignment 7

# function that prints a right angle triangle
def print_right_angle_triangle(n):
    for i in range(n, 0, -1):
        space = ' ' * (n - i)
        star = '*' * i
        print(space, star)


# function that prints an isosceles_triangle
def print_isosceles_triangle(n):
    for i in range(1, n + 1, 2):
        spaces = " " * ((n - i) // 2)
        stars = "*" * i
        print(spaces + stars)


# main program
try:
    n = int(input("Enter an odd positive integer: "))
    if n > 0:
        print_right_angle_triangle(n)
        print_isosceles_triangle(n)
    else:
        print("n must be positive")

except ValueError:
    print("Value Error: expected an intager.")
