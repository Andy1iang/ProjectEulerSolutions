# https://projecteuler.net/problem=3

'''
Learned:
--Prime Factorization Finds the largest prime divisor
  --Process: try to divide numerator by 2, if it can't, try 3, and so on, until square root of numerator,
             the numerator is largest prime divisor if end of loops hits, if numerator can be divided, 
             repeat the process with the new numerator and start at current denominator as the denominator
'''

from TimeCode import timeCode


def projectEuler3():
        
    def primeFac(num, divisor):

        # looping from denominator to sqrt of numerator
        for i in range(divisor, int(num**(1/2))+2):
            if num % i == 0:
                # recursive call if number could be divided
                return (primeFac(num/i, i))
            
        return int(num)

    print(primeFac(600851475143, 2))


timeCode(projectEuler3)
