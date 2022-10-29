n=int(input())
l1=list(map(int,input().split()))
m=int(input())
l2=list(map(int,input().split()))
b=[]
for i in range(n):
    b.insert(l2[i],l1[i])
print(*b)