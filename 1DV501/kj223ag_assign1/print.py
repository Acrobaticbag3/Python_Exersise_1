# assignment 1
s1, s2, s3, = "Knowledge", " is", " power!"

border = 9 * "==="              # create a border
border = "\n" + border          # used to get a clean base for the rectangle

space = 8 * "   "               # Create empty space
space = "\n| " + space + "|"    # Create the "walls" of our rectangle

print(s1, s2, s3, "\n")
print(s1, "\n ", s2, "\n", s3)
print(border, space,  "\n| ", s1, s2, s3, " |", space, border)
