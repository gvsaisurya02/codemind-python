n=int(input())
l=[]
re=[]
temp=n
flag=0
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        l.append(i)
while n>0:
    r=n%10
    re.append(r)
    n=n//10
for i in re:
    if i not in l:
        flag=1
        break
if flag==0 and temp in l:
    print("Mega Prime")
else:
    print("Not Mega Prime")