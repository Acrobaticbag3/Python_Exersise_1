# assignment 11
# returns the result of concatenating the string s with itself n times
def concat(s, n):
    s *= n
    print(s)


# returns the number of times the character x occurs in the string s
def count(s, x):
    temp = 0

    for i in range(len(s)):
        if s[i] == x:
            temp += 1

    print(f"The letter: {x}, in the srting '{s}' occurs {temp} times.")


# returns a string with all the characters in s in reverse order.
def reverse(s):
    lst = []

    # Iterate through the characters in s in reverse order
    for i in range(len(s) - 1, -1, -1):
        lst.append(s[i])

    # Join the list of characters into a string
    reversed_str = ''.join(lst)
    print(reversed_str)


# returns the first and last characters in the string s.
def first_last(s):
    if len(s) == 0:
        return None

    first_char = s[0]
    last_char = s[-1]
    print(first_char, last_char)


# return True if the string contains exactly two instances of the character X
def has_two_X(s):
    count = 0

    for i in range(len(s)):
        if s[i] == "x":
            count += 1

    return count == 2


# returns True if the string s contains any duplicate characters
def has_duplicates(s):
    seen = set()

    for char in s:
        if char in seen:
            return True
        seen.add(char)

    return False
