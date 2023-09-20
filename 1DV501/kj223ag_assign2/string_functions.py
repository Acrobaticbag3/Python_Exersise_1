def concat(s, n):   # returns the result of concatenating the string s with itself n times - Does not print correctly
    s *= n
    print(s)


def count(s, x):    # returns the number of times the character x occurs in the string s
    temp = 0

    for i in range(len(s)):
        if s[i] == x:
            temp += 1

    print(f"The letter: {x}, in the srting '{s}' occurs {temp} times.")


def reverse(s):     # returns a string with all the characters in s in reverse order.
    lst = []

    for i in range(len(s)):
        lst[] += i

    lst.reverse()
    return lst


def first_last(s):  # returns the first and last characters in the string s.
    pass       


def has_two_X(s):   # return True if the string contains exactly two instances of the character X
    count = 0

    for i in range(len(s)):
        if s[i] == "x":
            count += 1

        if count == 2:
            True
        else:
            False    


def has_duplicates(s):  # returns True if the string s contains any duplicate characters

    for i in range(len(s)):
        if s[i] == i:
            True
 