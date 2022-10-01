n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    for j in range(n):
        if l.index(i)!=j:
            if i==l[j]:
                break
            
    else:
        r.append(i)
if r==[]:
    print("-1")
else:
    for i in r:
        print(i,end=" ")