n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    s=str(i)
    r.append(s[::-1])
for j in r:
    print(int(j),end=" ")