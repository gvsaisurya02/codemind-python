n=int(input())
l=list(map(int,input().split()))
r=[]
for i in range(n):
    count=0
    for j in range(i+1,n):
        if l[i]<l[j]:
            count+=1
            break
        else:
            count+=1
            if count>0 and j==n-1:
                count=0
                break
    r.append(count)
for i in r:
    print(i,end=" ")