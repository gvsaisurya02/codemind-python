n=int(input())
c=0
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
for i in l:
    if i!=1 or i!=2:
        for j in range(2,i):
            if i%j==0:
                c+=1
                break
print(c+1)