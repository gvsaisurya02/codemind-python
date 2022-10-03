n=int(input())
l=[]
for i in range(n+1,100000):
    temp=i
    s=0
    while i>0:
        r=i%10
        s=(s*10)+r
        i=i//10
    if temp==s:
        l.append(temp)
        break
for j in range(n-1,1,-1):
    temp=j
    s1=0
    while j>0:
        r=j%10
        s1=(s1*10)+r
        j=j//10
    if temp==s1:
        l.append(temp)
        break
first=l[0]
second=l[1]
if abs(first-n)<abs(second-n):
    print(first)
elif abs(first-n)==abs(second-n):
    print(min(l),max(l))
else:
    print(second)