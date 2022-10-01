n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    r=[]
    for j in range(n):
        if l.index(i)!=j:
            if i>l[j]:
                r.append(i)
    print(len(r),end=" ")
