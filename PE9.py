#https://projecteuler.net/problem=9

from TimeCode import timeCode

def projectEuler9():
    #checking all a and b from 1 to 999
    for a in range(1,1000):
        for b in range(a+1,1000):
            c = (a**2 + b**2)**(1/2) #pythagorean theorem
            if (a + b + c) == 1000:
                print(int(a*b*c))

timeCode(projectEuler9)