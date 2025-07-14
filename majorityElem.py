import math
def majorityElem(arr):
    n = len(arr)
    help = dict()
    for i in range(n):
        if arr[i] not in help:
            help[arr[i]] = 1
        else:
            help[arr[i]]+=1
    
    for i in help:
        if help[i]>=math.floor(n/2):
            return i

print(majorityElem([1,2,3,2,4,2]))