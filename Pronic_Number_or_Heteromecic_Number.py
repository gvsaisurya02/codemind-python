n=int(input())
flag=0
for i in range(10):
    if i*(i+1)==n:
        print("YES")
        flag=1
        break
if flag==0:
    print("NO")