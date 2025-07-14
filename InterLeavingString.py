def InterLeavingString(s1,s2,s3):
    if (len(s1)+len(s2)==len(s3)):
        i,j,char = 0,0,0
        s4=""

        while char<len(s3):
            while i<len(s1) and char<len(s3) and s1[i]==s3[char]:
                s4+=s1[i]
                i+=1
                char+=1
                print(f"i = {i}")
                print(f"char = {char}")
                print(s4)
            
            while j<len(s2) and char<len(s3) and s2[j]==s3[char]:
                s4+=s2[j]
                j+=1
                char+=1
                print(f"j = {j}")
                print(f"char = {char}")
                print(s4)
            
            if char<len(s3):
                c = s3[char]

                if (i<len(s1) and j<len(s2)):
                    if (s1[i]!=c and s2[j]!=c):
                        return False
                if (i>=len(s1)):
                    if (s2[j]!=c):
                        return False
                elif (j>=len(s2)):
                    if (s1[i]!=c):
                        return False
                    
        return s4==s3
    else:
        return False
    
    

s1 = "aabcc"
s2 = "dbbca"
#s3 = "aadbbcbcac" ---True
s3 = "aadbbbaccc"
print(InterLeavingString(s1,s2,s3))
