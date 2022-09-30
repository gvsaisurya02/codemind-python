n=int(input())
m=int(input())
for i in range(n,m+1):
    l=[]
    temp=i
    while i>0:
        r=i%10
        l.append(r)
        i=i//10
    for j in l:
        if j>0:
            if temp%j!=0 or temp%10==0:
                break
    else:
        print(temp,end=" ")
        