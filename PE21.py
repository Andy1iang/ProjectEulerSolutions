# https://projecteuler.net/problem=21

from TimeCode import timeCode


def projectEuler21():

    possibles = {}
    finals = []

    # looping through all numbers
    # keeping track of the possible amicable numbers
    for i in range(1, 10000):
        sumDivis = sumDivisors(i)
        if sumDivis in possibles and possibles[sumDivis] == i:
            finals.append(i)
            finals.append(sumDivis)

        else:
            possibles[i] = sumDivis

    print(sum(finals))


# function to find the sum of all proper divisors of a number
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


timeCode(projectEuler21)
