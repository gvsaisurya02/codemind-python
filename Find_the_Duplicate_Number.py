n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    for j in range(n):
        if i==l[j] and l.index(i)!=j:
            r.append(i)
            break
s=set(r)
for i in s:
    print(i)