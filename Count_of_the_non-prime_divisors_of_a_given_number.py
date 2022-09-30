n=int(input())
l=[]
r=[]
p=0
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
for j in l:
    if j>2:
        for k in range(2,j):
            if j%k==0:
                r.append(j)
                break
print(len(r)+1)
        
    