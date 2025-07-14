import copy

def cavityMap(strArr):
    arr1 = []
    for i in range(len(strArr)):
        temp = []
        for j in range(len(strArr)):
            temp.append(int(strArr[i][j]))
        arr1.append(temp)

    arr2 = copy.deepcopy(arr1)
    for i in range(1, len(strArr) - 1):
        for j in range(1,len(strArr)-1):
            if i==0:
                left = arr1[i][j-1]
                right = arr1[i][j+1]
                down = arr1[i+1][j]
                if arr1[i][j] > left and arr1[i][j]>right and arr1[i][j]>down:
                    arr2[i][j]="X"

            
            elif i==len(strArr)-1:
                top = arr1[i-1][j]
                left = arr1[i][j-1]
                right = arr1[i][j+1]
                if arr1[i][j] > left and arr1[i][j]>right and arr1[i][j]>top:
                    arr2[i][j]="X"
            
            else:
                top = arr1[i-1][j]
                left = arr1[i][j-1]
                right = arr1[i][j+1]
                down = arr1[i+1][j]
                if arr1[i][j] > left and arr1[i][j]>right and arr1[i][j]>down and arr1[i][j]>top:
                    arr2[i][j]="X"
    

    ans = []
    for i in range(len(arr2)):
        str1 = ""
        for j in range(len(arr2)):
            str1+=str(arr2[i][j])
        ans.append(str1)
    
    return ans
        

strArr = ['1112', '1912', '1892', '1234']
print(cavityMap(strArr))