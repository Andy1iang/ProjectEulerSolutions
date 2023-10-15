#https://projecteuler.net/problem=7

'''
Learned:
Sieve of Eratosthenes: https://www.geeksforgeeks.org/sieve-of-eratosthenes/
'''

from TimeCode import timeCode

def projectEuler7():
    
    primeNums = []
    n = 10000000 #going up to 10 million
    nums = [True]*n #creating a 10 million long list filled from 0 to 10 million
    x = 2
    
    while x*x <= n: #going up to the root of 10 million
        if nums[x] is True: #when x is still labeled as possibly prime
            for i in range(x**2, n,x): #from square of x to n, each factor is not prime
                nums[i] = False
        
        x+=1
    
    for i in range(2,n):
        if nums[i] is True:
            primeNums.append(i) #putting all prime numbers in a list
            
    print(primeNums[10000]) #accessing the target value
    
    
timeCode(projectEuler7)