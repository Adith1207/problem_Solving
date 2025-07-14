def lilysHomework(arr):
    # Write your code here
    sArr = sorted(arr)
    help = dict()
    for i in arr:
        help[i] = arr.index(i)
    
    print(help)


print(lilysHomework([3,4,2,5,1]))


