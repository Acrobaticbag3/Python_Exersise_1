# assignment 17

# import just randint not the whole package random
from random import randint


lotto_sequance = []     # initialize enmpty list
CHECK = 7               # constant

# loop till we get 7 random numbers
print("The Lotto numbers this week:")
while len(lotto_sequance) < CHECK:
    lotto_num = randint(1, 35)

    if lotto_num not in lotto_sequance:
        lotto_sequance.append(lotto_num)

# sort the sequance of numbers & print result
lotto_sequance.sort()
print(*lotto_sequance, sep=' ')
