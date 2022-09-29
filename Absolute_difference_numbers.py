n,x=map(int,input().split())
l=n%pow(10,x)
x=str(x)
n=str(n)
ns=''
for i in range(int(x)):
    ns=ns+n[i]
print(abs(int(ns)-l))