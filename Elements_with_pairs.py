n=int(input())
l=list(map(int,input().split()))
if n%2!=0:
    print(*l,end=" ")
    print(0)
else:
    print(*l)
    