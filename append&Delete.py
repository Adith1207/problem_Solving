def appendAndDelete(s,t,k):
    l1 = s
    l2 = t

    if len(l1)==len(l2)==0 and k>=0:
        print("Yes")

    elif len(l1)==len(l2) and k>=2*len(l1):
        print("Yes")

    else:
        while l2.find(l1)==-1 and k!=0:
            if l1:
                l1 = l1[:-1]
            else:
                l1 = l1
            k-=1
        
        if (len(l2)-len(l1)<=k):
            k-=len(l2)-len(l1)
            if k!=0:
                if k%2==0:
                    print("Yes")
                else:
                    print("No")
            else:
                print("Yes")
        else:
            print("No")

s = "aabcc"
t = "aabbcc"
appendAndDelete(s,t,0)