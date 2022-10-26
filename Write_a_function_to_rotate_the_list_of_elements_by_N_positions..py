n=int(input())
l=list(map(int,input().split()))
r=int(input())
for i in range(r):
    temp=l[0]
    l[0]=l[n-1]
    for j in range(1,n):
        val=l[j]
        l[j]=temp
        temp=val
for i in l:
    print(i,end=" ")