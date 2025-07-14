def HowManyGames(p,d,m,s):
    sum = p
    count = 0
    while sum<=s:
        #print(sum)
        if (p-d)>=m:
            p = p-d
            sum+=p
        else:
            sum+=m
        
        count+=1
    
    return count


print(HowManyGames(16,2,1,9981))