n=int(input())
s=str(n)
r=s[::-1]
if n>0:
    print(int(r))
else:
    r=r[0:len(r)-1]
    r=int(r)
    print(-r)