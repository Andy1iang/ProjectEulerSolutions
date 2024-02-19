#Script used to time code (mostly for Project Euler)

'''
To Use:

from TimeCode import timeCode
timeCode(functionName)
'''

import time

def timeCode(function):
    t1 = time.time() #getting time before function runs
    function() 
    elapsed = time.time()-t1 #time after function runs - t1
    
    resFormat = 'Code Executed in: '
    
    #formatting the seconds & converting units to be more readable
    if elapsed < 0.000001:
        print(f'{resFormat}{elapsed*1000000:.3f} Microseconds')
    elif elapsed < 0.001:
        print(f'{resFormat}{elapsed*1000:.3f} Milliseconds')
    else:
        print(f'{resFormat}{elapsed:.3f} Seconds')