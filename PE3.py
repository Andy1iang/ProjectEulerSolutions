#https://projecteuler.net/problem=3

'''
Lessons:
--Prime Factorization Finds the largest prime divisor
  --Process: try to divide numerator by 2, if it can't, try 3, and so on, until square root of numerator,
             the numerator is largest prime divisor if end of loops hits, if numerator can be divided, 
             repeat the process with the new numerator and start at current denominator as the denominator
'''

from TimeCode import timeCode

def projectEuler3():
    
    def primeFac(num,divis):
        for i in range(divis,int(num**(1/2))+2): #looping from denominator to sqrt of numerator
            if num%i == 0:
                return(primeFac(num/i,i)) #recursive call if number could be divided
        return int(num)
    
    print(primeFac(600851475143,2))
    
timeCode(projectEuler3)