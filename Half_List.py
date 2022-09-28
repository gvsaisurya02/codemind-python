n=int(input())
l=list(map(int,input().split()))
for i in range(n-1,int(n/2)-1,-1):
    print(l[i],end=" ")
for i in range(0,int(n/2)):
    print(l[i],end=" ")
