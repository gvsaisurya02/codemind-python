n=int(input())
import math
s=0
l=list(map(int,input().split()))
for i in l:
    sqr=math.sqrt(i)
    if int(sqr)*int(sqr)==i:
        s=s+i
print(s)