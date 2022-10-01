n=int(input())
l=list(map(int,input().split()))
r=sorted(l)
re=[]
for i in r:
    re.append(i**2)
result=sorted(re)
for i in result:
    print(i,end=" ")