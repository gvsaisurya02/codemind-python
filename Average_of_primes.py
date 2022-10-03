n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    if i!=1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            r.append(i)
avg=sum(r)/len(r)
print("%.2f" %avg)