# assignment 19

# === === === Palindromes === === === #
# - "Was it a rat I saw?"
# - "A nut for a jar of tuna."
# - "Madam"
# - "Ni talar bra latin!"


# check if string is palindrome
def is_palindrome(s):
    # remove non-alphanumeric, convert to lowercase
    s = ''.join(c.lower() for c in s if c.isalnum())

    # is the string is equal to its reverse?
    return s == s[::-1]


# test cases, showcase and troubleshooting also, main program starts here
test_strings = [
    "Was it a rat I saw?",
    "A nut for a jar of tuna.",
    "Madam",
    "Ni talar bra latin!",
    "Hello, World!",
    "What was that?",
]


# loop through our test strings, check if palindrome
for i in test_strings:
    result = is_palindrome(i)
    if result:
        print(f'"{i}" is a palindrome? {result}')
    else:
        print(f'"{i}" is a palindrome? {result}.')
