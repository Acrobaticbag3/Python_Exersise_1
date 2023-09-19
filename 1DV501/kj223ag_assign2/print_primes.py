# assignment 5
def is_prime(n):
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


def print_primes(n):
    count = 0
    track = 0
    num = 0

    while count != n:
        num += 1

        if track == 10:
            track -= track
            print()

        else:
            if is_prime(num):
                count += 1
                track += 1
                print(num, end=' ')
            else:
                pass


userInput = int(input("How many primes? "))
print_primes(userInput)
