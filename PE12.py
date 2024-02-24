# https://projecteuler.net/problem=12

'''
Learned:
For most numbers, half of its divisors are under its square root (with the exception of perfect squares).
'''

from TimeCode import timeCode
import math


def projectEuler12():

    enoughDivisors = False
    num = 1
    idx = 1

    while enoughDivisors is False:

        divisors = 0

        for i in range(1, math.ceil(num**0.5)+1):
            if num % i == 0:
                divisors += 1

        divisors *= 2
        if num**0.5 == math.floor(num**0.5):  # account for perfect squares
            divisors -= 1

        if divisors > 500:
            enoughDivisors = True
        else:
            # incrementing according to triangle numbers
            idx += 1
            num += idx

    print(num)


timeCode(projectEuler12)
