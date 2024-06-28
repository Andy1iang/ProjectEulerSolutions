# https://projecteuler.net/problem=1

from TimeCode import timeCode


def projectEuler1():

    print(sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0]))


timeCode(projectEuler1)
