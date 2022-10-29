a=int(input())
l1=list(map(int,input().split()))
b=int(input())
l2=list(map(int,input().split()))
f=0
for i in l1:
    for j in l2:
        if i not in l2:
            f=1
            break
if f==0:
    print("True")
else:
    print("False")