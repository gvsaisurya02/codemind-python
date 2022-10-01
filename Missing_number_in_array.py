t=int(input())
for i in range(t):
    n=int(input())
    r=[]
    l=list(map(int,input().split()))
    for i in range(1,n+1):
        r.append(i)
    for i in r:
        if i not in l:
            print(i)