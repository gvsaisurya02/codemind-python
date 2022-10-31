s=input()
ma=0
c=0
for i in range(len(s)):
    c=0
    for j in range(i,len(s)):
        if s[i]==s[j] and s[j-1]==s[i] and i>0:
            c+=1
            if ma<c:
                ma=c
        else:
            break
print(ma+1)