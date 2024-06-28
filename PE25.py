# https://projecteuler.net/problem=25

from TimeCode import timeCode

def projectEuler25():

    a = 1
    b = 2

    count = 2

    while len(str(a)) < 1000:
        a, b = b, a + b
        count += 1

    print(count)

timeCode(projectEuler25)