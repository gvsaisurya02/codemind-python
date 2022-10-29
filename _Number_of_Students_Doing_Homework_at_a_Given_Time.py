n=int(input())
l1=list(map(int,input().split()))
m=int(input())
l2=list(map(int,input().split()))
qt=int(input())
c=0
for i in range(n):
    if qt in range(l1[i],l2[i]+1):
        c+=1
print(c)