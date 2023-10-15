#https://projecteuler.net/problem=6

'''
Learned: 
formula for sum of sequence of n numbers squared: https://www.cuemath.com/algebra/sum-of-squares/
'''

from TimeCode import timeCode

def projectEuler6():
    
    #formulas for sums
    sqSum = 100*101*201/6 
    sumSQ = (101*100/2)**2
    
    print(int(sumSQ-sqSum))
    

timeCode(projectEuler6)