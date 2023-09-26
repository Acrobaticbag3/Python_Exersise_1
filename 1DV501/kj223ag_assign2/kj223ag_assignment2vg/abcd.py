# assignment 13

# concatenat a, b, c, d to create a four digit number
def get_number(a, b, c, d):
    return a * 1000 + b * 100 + c * 10 + d


# iterate through various combinations of values
for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            for d in range(1, 10):
                # check that the right combination of values have been found
                if get_number(a, b, c, d) == 4 * get_number(d, c, b, a):
                    print(f"A = {a}, B = {b}, C = {c}, D = {d}")
