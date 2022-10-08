s=input()
flag=0
for i in range(len(s)):
    if s.count(s[i])==1:
        print(i)
        flag=1
        break
if flag==0:
    print(-1)