# https://projecteuler.net/problem=24

import itertools
from TimeCode import timeCode


def projectEuler24():

    # getting all permutations
    perms = [''.join(p) for p in itertools.permutations('0123456789')]

    # getting the millionth iterations
    print(perms[999999])


timeCode(projectEuler24)
