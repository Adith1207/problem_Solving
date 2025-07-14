def contaminated(str,target):
    l1 = list(str)
    c = 1

    while True:
        i=1
        deleted=False
        while i<len(l1):
            if l1[i]==target:
                del l1[i-1]
                deleted = True
                i = max(1,i-1)
            else:
                i+=1
        c+=1
        if not deleted:
            break
    
    return c

def contaminated1(str1,target):
    stack = []
    max_pass = 1

    for ch in str1:
        if ch==target and stack:
            prev_char, prev_pass = stack.pop()
            max_pass = max(max_pass,prev_pass+1)
        else:
            stack.append((ch,max_pass))
    
    return max_pass


str1 = 'abcdedaghded'
print(contaminated1(str1,'d'))
            
