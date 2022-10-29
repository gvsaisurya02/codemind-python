n=int(input())
l=list(map(int,input().split()))
l.sort()
l=set(l)
l=list(l)
if len(l)==3:
    print(min(l))
elif len(l)<3:
    print(max(l))
else:
    print(l[2])
