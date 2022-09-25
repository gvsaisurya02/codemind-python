n=int(input())
l=map(int,input().split())
e=[]
o=[]
for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
print(len(e),end=" ")
print(len(o))
