#https://projecteuler.net/problem=5 

from TimeCode import timeCode

def ProjectEuler5():
    
    ans = -1
    num = 20
    
    while ans < 0:
        #checking all possible divisors (i.e. if divisible by 20, then its divisible by 10, 5, etc.)
        if num%20 == 0 and num%19 == 0 and num%18 == 0 and num%17 == 0 and num%16 == 0 and num%15 == 0 and num%14 == 0 and num%13 == 0 and num%12 == 0 and num%11 == 0:
            ans = num
        num+=20

    print(ans)
    
timeCode(ProjectEuler5)
        