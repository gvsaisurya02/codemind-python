n=int(input())
l=list(map(int,input().split()))
r=[]
for i in range(0,n,2):
    for j in range(l[i+1]):
        r.append(l[i])
for i in r:
    print(i,end=" ")