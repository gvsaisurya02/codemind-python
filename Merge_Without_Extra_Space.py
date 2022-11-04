t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    rl=l+l2
    print(*sorted(rl))