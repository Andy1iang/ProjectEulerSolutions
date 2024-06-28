# https://projecteuler.net/problem=6

'''
Learned: 
formula for sum of sequence of n numbers squared: https://www.cuemath.com/algebra/sum-of-squares/
'''

from TimeCode import timeCode


def projectEuler6():

    n = 100

    # formulas for sums
    sqSum = n*(n+1)*(2*n+1)/6
    sumSQ = (n*(n+1)/2)**2

    print(int(sumSQ-sqSum))


timeCode(projectEuler6)
