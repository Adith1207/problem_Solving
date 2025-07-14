def divisibleSumPairs(n, k, ar):
    # Write your code here
    c=0
    for i in range(n):
        for j in range(i+1,n):
            if (i<j and (ar[i]+ar[j])%k==0):
                c+=1
    return c

l1 = [1,3,2,6,1,2]
print(divisibleSumPairs(6,3,l1))