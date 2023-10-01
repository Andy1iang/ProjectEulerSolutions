#https://projecteuler.net/problem=1

from TimeCode import timeCode

def projectEuler1():
    sum = 0
    
    #adding every third number
    for num in range(3,1000,3):
        sum += num
        
    #adding every fifth number from 5 and 10, because 15 and it's multiples are divisible by 3
    for num in range(5,1000,15):
        sum+=num
        
    for num in range(10,1000,15):
        sum+=num
            
    print(sum)

timeCode(projectEuler1)