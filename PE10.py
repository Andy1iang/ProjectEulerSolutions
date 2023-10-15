#https://projecteuler.net/problem=10

from TimeCode import timeCode

def projectEuler10():
    n = 2000001
    nums = [True]*n
    x = 2
    
    #Sieve of Eratosthenes
    while x**2 <= n:
        if nums[x] is True:
            for i in range(x**2,n,x):
                nums[i] = False
                
        x+=1

    sum = 0
    for i in range(2,n):
        if nums[i] is True:
           sum += i
           
    print(sum) 
    
    
timeCode(projectEuler10)