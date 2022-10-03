n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
r=[]
result=[]
for i in l1:
    if i in l2 and i not in r:
        result.append(i)
        r.append(i)
print(len(result))