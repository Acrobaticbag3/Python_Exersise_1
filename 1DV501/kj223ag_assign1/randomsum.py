# assignment 13
import random

rnd_int_arr = [random.randint(1, 100) for _ in range(5)]    # init a randome array of ints
sum = sum(rnd_int_arr)                                      # sum of all elements in the array

# convert the int array elements into strings and then join them and leave a space inbetween
convert_to_String = ' '.join(map(str, rnd_int_arr))

print("Five randome numbers:", convert_to_String, "\n The sum is:",sum)