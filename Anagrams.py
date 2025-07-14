def anagram(s):
    # Write your code here
    if len(s)%2 !=0 :
        return -1
    
    l1 = s[0:len(s)//2]
    l2 = s[len(s)//2:len(s)]

    help1 = dict()
    help2 = dict()    
    c =0
    for char in l1:
        if char not in help1:
            help1[char]=1
        else:
            help1[char]+=1
    

    for char in l2:
        if char not in help2:
            help2[char]=1
        else:
            help2[char]+=1
    
    for i in help1:
        c += max(0, help1[i]-help2.get(i,0))
    
    return c

print(anagram("aaabbb"))
    
