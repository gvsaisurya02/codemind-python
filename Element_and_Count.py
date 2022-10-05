n=int(input())
l=list(map(int,input().split()))
r=[]
re=[]
for i in l:
    if i not in re:
        r.append(i)
        r.append(l.count(i))
        re.append(i)
for i in r:
    print(i,end=" ")