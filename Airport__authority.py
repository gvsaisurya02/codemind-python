n=int(input())
l=[]
s=0
for i in range(n):
    val=int(input())
    l.append(val)
t=int(input())
for i in l:
    if i>t:
        s=s+2
    else:
        s=s+1
print(s)