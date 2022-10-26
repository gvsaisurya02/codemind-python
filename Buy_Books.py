n=int(input())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
sl=sum(l)
s1=sum(l1)
if sl>s1:
    print("0")
else:
    print(s1-sl)