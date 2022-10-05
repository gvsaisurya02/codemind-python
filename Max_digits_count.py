n=int(input())
l=list(map(int,input().split()))
maxi=max(l)
s=str(maxi)
c=0
for i in l:
    s1=str(i)
    if len(s1)==len(s):
        c=c+1
print(c)