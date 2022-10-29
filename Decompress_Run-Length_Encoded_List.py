n=int(input())
l=list(map(int,input().split()))
b=[]
for i in range(0,n,2):
    for j in range(l[i]):
        b.append(l[i+1])
        
print(*b)