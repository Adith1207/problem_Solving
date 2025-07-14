def theLoveLetterMystery(s):
    count = 0
    i=0
    for char in range(len(s)-1,-1,-1):
        if s[char] != s[i] and s[char]!='a' and s[char]>s[i]:
            count+= ord(s[char])-ord(s[i])
        i+=1
    return count

print(theLoveLetterMystery('cba'))