n=int(input())
s=0
if n>0:
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    print(s)
else:
    r=str(n)[::-1]
    f=r[0:len(r)-1]
    fr="-"+f
    print(int(fr))