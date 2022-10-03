n=int(input())
m=int(input())
for i in range(n,m+1):
    flag=0
    l=[]
    temp=i
    while i>0:
        r=i%10
        l.append(r)
        i=i//10
    for j in l:
        if j!=0:
            if temp%j!=0:
                flag=1
        else:
            flag=1
    if flag==0:
        print(temp,end=" ")
        