# https://projecteuler.net/problem=5

from TimeCode import timeCode


def ProjectEuler5():

    num = 20

    while True:

        # checking all possible divisors (i.e. if divisible by 20, then its divisible by 10, 5, etc.)
        if num % 20 == 0 and num % 19 == 0 and num % 18 == 0 and num % 17 == 0 and num % 16 == 0 and num % 15 == 0 and num % 14 == 0 and num % 13 == 0 and num % 12 == 0 and num % 11 == 0:
            print(num)
            break

        num += 20


timeCode(ProjectEuler5)
