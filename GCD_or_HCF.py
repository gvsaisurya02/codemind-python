n,m=map(int,input().split())
ln=[]
lm=[]
for i in range(1,n+1):
    if n%i==0:
        ln.append(i)
for j in range(1,m+1):
    if m%j==0:
        lm.append(j)
a=set(ln)
b=set(lm)
r=a.intersection(b)
print(max(r))