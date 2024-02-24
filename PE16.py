# https://projecteuler.net/problem=16

from TimeCode import timeCode


def projectEuler16():

    num = 2**1000
    num = str(num)
    num = list(map(int, list(num)))  # getting sum of digits

    print(sum(num))


timeCode(projectEuler16)
