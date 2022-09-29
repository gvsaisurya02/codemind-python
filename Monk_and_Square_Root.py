t=int(input())
for i in range(t):
    l=[]
    n,m=map(int,input().split())
    for j in range(m):
        if (j*j)%m==n:
            l.append(j)
    if l!=[]:
        print(min(l))
    else:
        print("-1")
    