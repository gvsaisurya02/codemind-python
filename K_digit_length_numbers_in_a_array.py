n,m=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    if i>=0:
        if len(str(i))==m:
            c+=1
    else:
        if len(str(i))-1==m:
            c+=1
        
print(c)