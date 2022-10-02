n=int(input())
l=list(map(int,input().split()))
flag=0
x=[]
y=[]
for i in l:
    if flag==0:
        x.append(i)
        flag=1
    else:
        y.append(i)
        flag=0
xs=sum(x)
ys=sum(y)
if abs(xs-ys)%4==0:
    print("X")
else:
    print("Y")