n=int(input())
for i in range(n+1,100000,1):
    s=str(i)
    rev=s[::-1]
    if int(rev)==i:
        for j in range(2,i):
            if i%j==0:
                break;
        else:
            print(i)
            break