n=int(input())
pd,sd=0,0
for i in range(n):
    l=list(map(int,input().split()))
    for j in range(n):
        if i==j:
            pd+=l[j]
        if i+j==n-1:
            sd+=l[j]
print("Principal Diagonal:",end="")
print(pd)
print("Secondary Diagonal:",end="")
print(sd)