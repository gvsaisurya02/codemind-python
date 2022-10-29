n=int(input())
l=list(map(int,input().split()))
t=int(input())
for i in range(0,n):
    if l[i]==t:
        print(i,end=" ")
        break
else:
    print("-1",end=" ")
for j in range(n-1,-1,-1):
    if l[j]==t:
        print(j)
        break
else:
    print("-1",end=" ")