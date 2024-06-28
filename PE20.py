# https://projecteuler.net/problem=20

from TimeCode import timeCode

import math


def projectEuler20():
    print(sum(int(i) for i in str(math.factorial(100))))  # one-liner ;)


timeCode(projectEuler20)
