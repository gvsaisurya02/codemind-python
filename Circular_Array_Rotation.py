a,b,c=map(int,input().split())
l=list(map(int,input().split()))
l2=[]
for i in range(c):
    v=int(input())
    l2.append(v)
for i in range(b):
    temp=l[0]
    l[0]=l[a-1]
    for j in range(1,a):
        val=l[j]
        l[j]=temp
        temp=val
for i in l2:        
    print(l[i])