n=int(input())
l=list(map(int,input().split()))
e=int(input())
r=[]
maxi=max(l)
for i in l:
    if i+e>=maxi:
        r.append("True")
    else:
        r.append("False")
for i in r:
    print(i,end=" ")