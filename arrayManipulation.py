def arrayManipulation(n, queries):
    # Write your code here
    ans = [[0 for i in range(n)]]
    for i in range(len(queries)):
        temp = ans[i]
        first = queries[i][0]-1
        last = queries[i][1]-1
        k = queries[i][2]
        for j in range(n):
            if j>=first and j<=last:
                temp[j]+= k
        ans.append(temp)
    
    return max(ans[0])

arrayManipulation(10, [[1,5,3],[4,8,7],[6,9,1]])