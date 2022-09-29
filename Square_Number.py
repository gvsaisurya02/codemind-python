n=int(input())
flag=0
for i in range(1,n):
    for j in range(0,i):
        if (i**2)+(j**2)==n:
            flag=1
if flag==1:
    print("True")
else:
    print("False")