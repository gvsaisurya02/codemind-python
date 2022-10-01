n=int(input())
l=list(map(int,input().split()))
r=[]
maxi=max(l)
for i in l:
    if i<=maxi and i!=0:
        r.append(i)

co=l.count(0)
for j in range(co):
    r.append(0)
for j in r:
    print(j,end=" ")