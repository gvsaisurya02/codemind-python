n=int(input())
l=list(map(int,input().split()))
b=[]
c=0
for i in l:
    if i not in b:
        b.append(i)
        if i%2!=0:
            c+=1
print(c)
