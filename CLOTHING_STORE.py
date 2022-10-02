n=int(input())
coun=0
l=list(map(int,input().split()))
r=[]
re=[]
for i in l:
    if i not in r:
        c=l.count(i)
        if c>1:
            re.append(c//2)
            r.append(i)
print(sum(re))