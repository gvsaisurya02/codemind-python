n=input()
rev=n[::-1]
n=int(n)
rev=int(rev)
flag,flag1=0,0
for i in range(2,n):
    if n%i==0:
        break
else:
    flag=1
for j in range(2,rev):
    if rev%j==0:
        break
else:
    flag1=1
if flag==1 and flag1==1:
    print("circular prime")
elif flag==1 and flag1==0:
    print("prime but not a circular prime")
elif flag==0 and flag1==0:
    print("not prime")