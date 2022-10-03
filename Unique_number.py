n=int(input())
s=str(n)
l=[]
flag=0
for i in s:
    l.append(i)
for i in l:
    if l.count(i)!=1:
        flag=1
if flag==1:
    print("Not Unique Number")
else:
    print("Unique Number")
    
    