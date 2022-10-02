n,m=map(int,input().split())
l=list(map(int,input().split()))
ll=[]
skip=0
for i in l:
    if i<=m:
        if skip==1 or skip==0:
            ll.append(i)
    else:
        skip=skip+1
print(len(ll))