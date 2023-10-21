#https://projecteuler.net/problem=12

'''
Learned:
For most numbers, half of its divisors are under its square root
'''

from TimeCode import timeCode
import math

def projectEuler12():
    
    enoughDivisors = False
    idx = 1
    
    while enoughDivisors is False:
        
        triVal = idx*(idx+1)//2
        divisors = 0
        
        for i in range(1,math.ceil(triVal**0.5)+1):
            if triVal % i == 0:
                divisors += 1
        
        divisors *= 2
        if divisors > 500:
            enoughDivisors = True
                
        idx += 1
                
    print(triVal)
    
timeCode(projectEuler12)