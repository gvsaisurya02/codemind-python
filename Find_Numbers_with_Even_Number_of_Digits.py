n=int(input())
import math
c=0
l=list(map(int,input().split()))
for i in l:
    d=math.floor(math.log10(i))+1
    if d%2==0:
        c+=1
print(c)