def alternatingCharacters(s):
    count = 0
    stack = []
    stack.append(s[0])
    for c in range(1,len(s)):
        print(stack[-1])
        if stack[-1]==s[c]:
            count+=1
        else:
            stack.append(s[c])
    
    return count

print(alternatingCharacters('AAAA'))