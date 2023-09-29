import time

def timeCode(function):
    t1 = time.time()
    function() 
    elapsed = time.time()-t1
    if elapsed < 0.000001:
        print(f'{elapsed*1000000:.3f} microseconds')
    elif elapsed < 0.001:
        print(f'{elapsed*1000:.3f} milliseconds')
    else:
        print(f'{elapsed:.3f} seconds')