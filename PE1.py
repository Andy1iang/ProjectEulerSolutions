from TimeCode import timeCode

def projectEuler1():
    sum = 0
    for num in range(3,1000,3):
        sum += num
    for num in range(5,1000,5):
        if num%3 != 0:
            sum+=num
            
    print(sum)

timeCode(projectEuler1)