n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
r=[]
for i in l1:
    if i not in l2:
        r.append(i)
for j in l2:
    if j not in l1:
        r.append(j)
s=set(r)
print(len(s))