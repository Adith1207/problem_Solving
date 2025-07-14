def marsExploration(s):
    test = 'SOS'
    c = 0
    i,j = 0,0
    while j<len(s):
        if (test[i]!=s[j]):
            c+=1
            j+=1

            if (i+1<len(test)):
                i+=1
            else:
                i=0
            
        
        else:
            j+=1
            if (i+1<len(test)):
                i+=1
            else:
                i=0
    
    return c

    

print(marsExploration('SOSSPSSQSSOR'))