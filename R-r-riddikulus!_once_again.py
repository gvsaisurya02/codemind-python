n,m=map(int,input().split())
l=list(map(int,input().split()))
ll=[]
rl=[]
for i in range(m):
    ll.append(l[i])
for j in range(m,n):
    rl.append(l[j])
for i in rl:
    print(i,end=" ")
for j in ll:
    print(j,end=" ")