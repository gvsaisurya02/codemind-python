s=input()
flag=0
for i in range(len(s)):
    for j in range(len(s)):
        if i!=j:
            if s[i]==s[j]:
                flag=1
                break
if flag==1:
    print("False")
else:
    print("True")