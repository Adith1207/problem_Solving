import heapq
def cookies(k,A):
    heapq.heapify(A)
    c = 0

    while A[0]<k and len(A)>=2:
        sum=0
        minVal = heapq.heappop(A)
        minVal1 = heapq.heappop(A)
        sum = minVal + 2*minVal1
        heapq.heappush(A,sum)
        c+=1
    
    if A and A[0]>k:
        return c
    return -1
