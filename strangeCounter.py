def strangeCounter(t):
    cycleStart = 3
    cycle = 1
    while t> cycle + cycleStart-1:
        cycle += cycleStart
        cycleStart*=2
    
    return cycleStart - (t-cycle)
'''
    ---------PROBLEM : Exceeds the time limit---------------
    mainVal = 3
    val = mainVal
    for i in range(1,t):
        if val!=1:
            val-=1
        else:
            mainVal*=2
            val = mainVal
        print(val)
    
    return val
'''
    
 
t = 4
print(strangeCounter(t))