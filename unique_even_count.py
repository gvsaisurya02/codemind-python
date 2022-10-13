n=int(input())
l=list(map(int,input().split()))
s=0
r=[]
for i in range(n):
    for j in range(n):
        if i!=j:
            if l[i]==l[j]:
                r.append(l[i])
                break
    else:
        r.append(l[i])
r=set(r)
for i in r:
    if i%2==0:
        s+=1
print(s)