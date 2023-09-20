# assignment 11
def inc(n):           # Increments n with one
    n += 1
    return n


def inc_with(n, t):   # Increments n with the value of t
    n += t
    return n


def greatest(n1, n2):   # Returns the largest of the values n1 and n2
    if n1 > n2:
        return n1
    elif n1 == n2:
        print("")
    else:
        return n2


def is_even(n):     # Returns True if n is even, otherwise false
    if n % 2 == 0:
        return True
    else:
        return False


def power(x, n):    # Returns x to the power of n
    i = x ** n
    return i


def factorial(n):   # Returns the factorial of n
    for i in range(n-1, 1, -1):
        n *= i
    return n


def is_prime(n):    # Returns True if n is a prime, otherwise false
    if n <= 1:                  # Primes can only be positive
        return False
    elif n <= 3 and n != 1:     # 2,3 are primes
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


print('41 plus 1:', inc(41))
print('30 plus 12:', inc_with(30, 12))

print('Which is greater, 24 or 42?', greatest(24, 42))

print('Is 42 even?: ', is_even(42))

print('2 to the power of 10:', power(2, 10))

print('Factorial of 5:', factorial(5))

print('Is 41 a prime?:', is_prime(41))
