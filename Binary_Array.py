n=int(input())
l=list(map(int,input().split()))
flag=0
for i in l:
    if i!=0 and i!=1:
        flag=1
        break
if flag==1:
    print("False")
else:
    print("True")