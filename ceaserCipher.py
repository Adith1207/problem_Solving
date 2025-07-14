def caesarCipher(s, k):
    helpSmall = [chr(i) for i in range(ord('a'),ord('z')+1)]
    helpBig = [chr(i) for i in range(ord('A'),ord('Z')+1)]
    ans = ''
    for i in s:
        if i.isalpha():
            if i.islower():
                ind = helpSmall.index(i)
                ind = (ind + k)%26
                ans += helpSmall[ind]
            
            else:
                ind = helpBig.index(i)
                ind = (ind + k)%26
                ans += helpBig[ind]
        else:
            ans+=i
    
    return ans

print(caesarCipher('ab-Z',1))
