# assignment 11
import random
rndNumbOne = random.randint(-10, 10)    # give random int

if rndNumbOne < 0:      # is positive?
    if rndNumbOne % 2 == 0:     # even?
        print(f"{rndNumbOne} is a negative and even number.")
    if rndNumbOne % 2 != 0:     # odd?
        print(f"{rndNumbOne} is a negative and odd number.")

elif rndNumbOne > 0:    # is negative?
    if rndNumbOne % 2 == 0:     # even?
        print(f"{rndNumbOne} is a posetive and even number.")
    if rndNumbOne % 2 != 0:     # odd?
        print(f"{rndNumbOne} is a posetive and odd number.")

elif rndNumbOne == 0:   # check for 0
    print(f"{rndNumbOne} is even and neither positive nor negative.")
else:   # default/fallback case
    print("Something whent wrong!")