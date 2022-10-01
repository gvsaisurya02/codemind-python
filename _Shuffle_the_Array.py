n=int(input())
l=list(map(int,input().split()))
left=[]
right=[]
for i in range(0,int(n/2)):
    left.append(l[i])
for j in range(int(n/2),n):
    right.append(l[j])
i=0
while i<int(n/2):
    print(left[i],end=" ")
    print(right[i],end=" ")
    i+=1