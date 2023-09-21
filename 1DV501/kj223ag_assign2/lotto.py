# assignment 17
from random import randint

lotto_sequance = []
CHECK = 7

print("The Lotto numbers this week:")
while len(lotto_sequance) < CHECK:
    lotto_num = randint(1, 35)

    if lotto_num not in lotto_sequance:
        lotto_sequance.append(lotto_num)

lotto_sequance.sort()
print(*lotto_sequance, sep=' ')
