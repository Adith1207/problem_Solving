def rotateAndFlip(arr1,angle,flip):
    final = []
    if angle==90 or angle==270:
        for i in range(len(arr1)-1,-1,-1):
            temp = []
            for j in range(len(arr1)):
                temp.append(arr1[i][j])
            final.append(temp)
        
        transpose = [[0]*len(final) for i in range(len(final))]
        for i in range(len(final)):
            for j in range(len(final)):
                transpose[i][j] = final[j][i]
        
        ans = flip1(transpose,flip)
        return ans
    
    elif angle==180:
        final = arr1
        ans = flip1(final,flip)
        return ans
    

def flip1(arr1,flip):
    final = []
    if flip=='v':
        for i in range(len(arr1)):
            temp = []
            for j in range(len(arr1)-1,-1,-1):
                temp.append(arr1[i][j])
            final.append(temp)
        return final
    
    else:
        for i in range(len(arr1)-1,-1,-1):
            temp=[]
            for j in range(len(arr1)):
                temp.append(arr1[i][j])
            final.append(temp)
        return final
                




arr1 = [[1,0,0],[0,1,1],[0,0,1]]
print(rotateAndFlip(arr1,180,'v'))



