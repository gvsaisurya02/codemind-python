n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
r=[]
for i in l1:
    if i in l2 and i not in r:
        print(i,end=" ")
        r.append(i)
