#https://projecteuler.net/problem=15

'''
Learned:
When limited to 2 directional movements,
the total path options are limited to (total moves to get to point B)! divided by 
the product of (moves in one direction)! and (moves in other directions)!
'''

from TimeCode import timeCode
from math import factorial

def projectEuler15():
    
    res = factorial(40) / (factorial(20)*factorial(20))
    
    print(int(res))
    
timeCode(projectEuler15)