#https://projecteuler.net/problem=14

from TimeCode import timeCode

def projectEuler14():
    
    largest = 0
    largestIdx = -1
    for i in range(1,1000000):
        
        steps = 0
        num = i
        #following the Collatz Sequences
        while num != 1:
            steps += 1
            if num%2 == 0:
                num = num//2
            else:
                num = 3*num + 1
        
        if steps > largest:
            largest = steps
            largestIdx = i
            
    print(largestIdx)
            
timeCode(projectEuler14)