def repeatedString(s,n):
    c = 0
    if s=='':
        return c

    else:
        for char in s:
            if char=='a':
                c+=1
        
        multiplier = n//len(s)
        c = c*multiplier

        adder = n%len(s)
        for i in range(0,adder):
            if s[i]=='a':
                c+=1
        
        
        return c
        

s = 'a'
n = 1000000000000
print(repeatedString(s,n))