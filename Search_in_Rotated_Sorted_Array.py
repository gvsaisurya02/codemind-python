n=int(input())
l=list(map(int,input().split()))
p=int(input())
flag=0
for i in range(n):
    if l[i]==p:
        flag=1
        break
if flag==1:
    print(i)
else:
    print("-1")