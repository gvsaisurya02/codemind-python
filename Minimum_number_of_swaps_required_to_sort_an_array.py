n=int(input())
l=list(map(int,input().split()))
temp=l.copy()
temp.sort()
c=0
for i in range(n):
    if l[i]!=temp[i]:
        c+=1
        ind=l.index(temp[i])
        l[i],l[ind]=l[ind],l[i]
print(c)