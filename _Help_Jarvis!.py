t=int(input())
for i in range(t):
    n=int(input())
    if n==0:
        print("YES")
    else:
        b=[]
        while n>0:
            b.append(n%10)
            n=n//10
        f=0
        b.sort()
        for i in range(len(b)-1):
            if b[i+1]-b[i]!=1:
                f=1
    if f==1:
        print("NO")
    else:
        print("YES")
        
    