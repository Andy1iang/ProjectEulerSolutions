# https://projecteuler.net/problem=808

from TimeCode import timeCode


def projectEuler808():

    primes = sievePrimes(int(1E8))
    primeSquared = {x**2 for x in primes}  # putting square of primes in a set

    total = 0
    count = 0
    for num in primeSquared:

        strNum = str(num)
        # checking conditions
        if strNum != strNum[::-1] and int(strNum[::-1]) in primeSquared:
            count += 1
            total += num

        if count == 50:
            break

    print(total)


# getting all primes
def sievePrimes(limit):

    # using the Sieve of Eratosthenes
    primes = []
    checker = [True for i in range(limit+1)]
    n = 2
    while (n <= limit**0.5):

        if checker[n] is True:

            for i in range(n*n, limit+1, n):

                checker[i] = False

        n += 1

    for i in range(2, limit+1):
        if checker[i] is True:
            primes.append(i)

    return primes


if __name__ == "__main__":
    timeCode(projectEuler808)
