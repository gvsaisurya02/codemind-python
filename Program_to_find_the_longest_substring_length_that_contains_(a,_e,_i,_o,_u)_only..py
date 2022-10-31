s=input()
maxi=0
c=0
for i in range(len(s)):
    c=0
    for j in range(i,len(s)):
            if s[i] in "aeiou":
                if s[j] in "aeiou":
                    c+=1
                else:
                    break
    if maxi<c:
        maxi=c
print(maxi)