def kaprekarNumbers(p, q):
    ans = []
    for num in range(p,q+1):
        strNum = str(num)
        dig = len(strNum)
        sq = num*num
        strSq = str(sq)
        digSq = len(strSq)
        
        left = strSq[:digSq//2]
        right = strSq[digSq//2:]

        if left=='':
            left='0'

        if (int(left)+int(right)==num):
            ans.append(num)
    
    if len(ans)==0:
        return "INVALID RANGE"
    return ans

print(kaprekarNumbers(1,100))