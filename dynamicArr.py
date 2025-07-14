def dynamicArray(n, queries):
    # Write your code here
    arr = [[] for i in range(n)]
    lastAns = 0
    ans = []
    
    for q in queries:
        if q[0]==1:
            idx = q[1]^lastAns
            arr[idx].append(q[2])
        elif q[0]==2:
            idx = (q[1]^lastAns)%2
            lastAns = arr[idx][q[2]%len(arr[idx])]
            ans.append(lastAns)
    
    return ans

queries = [[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]]
print(dynamicArray(2,queries))