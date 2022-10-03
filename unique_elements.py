n=int(input())
l=list(map(int,input().split()))
flag=0
r=[]
re=[]
for i in l:
    if l.count(i)==1 or i not in r:
        re.append(i)
        r.append(i)
for i in re:
    print(i,end=" ")