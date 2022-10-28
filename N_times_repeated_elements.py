n=int(input())
l=list(map(int,input().split()))
b=[]
flag=0
k=int(input())
for i in l:
    if l.count(i)==k and i not in b:
        b.append(i)
        flag=1
if flag==0:
    print("-1")
else:
    print(*b)