n=int(input())
l=list(map(int,input().split()))
b=[]
for i in range(n-1):
    nl=l[i+1::1]
    b.append(max(nl))
b.append(-1)
print(*b)