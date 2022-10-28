n=int(input())
l=list(map(int,input().split()))
b=[]
flag=0
for i in l:
    if l.count(i)==i and i not in b:
        b.append(i)
        flag=1
print(len(b))