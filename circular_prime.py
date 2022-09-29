n=int(input())
n=str(n)
p,rp=0,0
r=n[::-1]
for i in range(2,int(n)):
    if int(n)%i==0:
        p=1
for i in range(2,int(r)):
    if int(r)%i==0:
        rp=1
if p==0 and rp==0:
    print("circular prime")
elif p==0 and rp!=0:
    print("prime but not a circular prime")
else:
    print("not prime")