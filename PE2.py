#https://projecteuler.net/problem=2

from TimeCode import timeCode

def projectEuler2():
    a = 0
    b = 1
    sum = 0
    while b <= 4000000:
        
        if b%2 == 0:
            sum+=b
            
        a,b = b,a+b
        
    print(sum)

timeCode(projectEuler2)