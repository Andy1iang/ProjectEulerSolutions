# https://projecteuler.net/problem=23

from TimeCode import timeCode


def projectEuler23():

    total = 0
    abundants = set()

    # going to upper limit & finding all abundant numbers
    for i in range(1, 28123):
        if sumDivisors(i) > i:
            abundants.add(i)

    # checking if the number can be represented as the sum of two abundant numbers
    for i in range(1, 28123):
        for a in abundants:
            if (i - a) in abundants:
                break
        else:
            total += i

    print(total)

# function to get sum of divisors


def sumDivisors(n):

    total = 0

    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            total += i
            total += n//i

    total -= n
    if n**0.5 == int(n**0.5):
        total -= int(n**0.5)

    return total


timeCode(projectEuler23)
