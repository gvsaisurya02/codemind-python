n=int(input())
l=[]
flag=0
r=[]
for i in range(1,n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        l.append(i)
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if n==l[i]*l[j]:
            r.append(l[i])
            r.append(l[j])
            flag=1
            break
if flag==1:
    for val in r:
        print(val,end=" ")
else:
    print(-1)