#https://projecteuler.net/problem=67

from TimeCode import timeCode

def projectEuler67():
    
    pyramid = open('PE67.txt','r').read()
    
    levels = [list(map(int,x.strip().split())) for x in pyramid.strip().split('\n')]
    levels.reverse()

    for i in range(1, len(levels)):

        for j in range(len(levels[i])):
            levels[i][j] += max(levels[i-1][j], levels[i-1][j+1])
            


    print(levels[-1][0])
    

timeCode(projectEuler67)