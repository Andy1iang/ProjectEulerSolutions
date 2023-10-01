#Script used to time code (mostly for Project Euler)

import time

def timeCode(function):
    t1 = time.time() #getting time before function runs
    function() 
    elapsed = time.time()-t1 #time after function runs - t1
    
    #formatting the seconds & converting units to be more readable
    if elapsed < 0.000001:
        print(f'{elapsed*1000000:.3f} microseconds')
    elif elapsed < 0.001:
        print(f'{elapsed*1000:.3f} milliseconds')
    else:
        print(f'{elapsed:.3f} seconds')