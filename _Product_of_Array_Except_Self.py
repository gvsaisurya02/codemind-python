n=int(input())
l=list(map(int,input().split()))
p=1
for i in l:
    p=1
    for j in range(n):
        if i!=l[j]:
            p=p*l[j]
    print(p,end=" ")