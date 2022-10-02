n=int(input())
coun=0
l=list(map(int,input().split()))
r=[]
maxi=-1
maximum=-1
for i in l:
    c=l.count(i)
    if c>maxi and i not in r:
        maxi=l.count(i)
        maximum=i
        r.append(i)
print(maximum)