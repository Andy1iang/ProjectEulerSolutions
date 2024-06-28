# https://projecteuler.net/problem=22

from TimeCode import timeCode

def projectEuler22():

    total = 0 

    names = open('PE22.txt').read().replace('"','').split(',')
    names.sort()

    for idx,name in enumerate(names):
        score = 0
        for char in name:
            score += ord(char) - 64
        total += score * (idx+1)

    print(total)


projectEuler22()