def superReducedString(s):
    l1 = list(s)
    i,j = 0,1
    while i<len(l1) and j<len(l1):
        if l1[i]==l1[j]:
            del l1[j]
            del l1[i]
            i,j=0,1
        else:
            i+=1
            j+=1
    
    if len(l1)!=0:
        return ''.join(l1)
    
    return "Empty String"


s = "abba"
print(superReducedString(s))