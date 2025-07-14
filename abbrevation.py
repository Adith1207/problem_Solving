def abbrevation(a,b):
    if len(a)>=len(b):
        i,j = 0,0
        while i<len(a):
            print(f"0i = {i}")

            if j==len(b) and i<len(a):
                if a[i].isupper():
                    return 'NO'
                else:
                    i+=1
                    print(f"1i = {i}")
                

            elif a[i].isupper():
                if a[i]==b[j]:
                    i+=1
                    j+=1
                    print(f"2i = {i}")
                else:
                    return 'NO'
            
            elif a[i].islower():
                if a[i]==b[j].lower():
                    i+=1
                    j+=1
                    print(f"3i = {i}")
                
                else:
                    i+=1
                    print(f"4i = {i}")
        
        if j != len(b):
            return 'NO'
        else:
            return 'YES'
    else:
        return 'NO'


a = 'PabcdD'
b = 'PBD'
print(abbrevation(a,b))