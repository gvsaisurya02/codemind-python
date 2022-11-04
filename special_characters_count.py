s=input()
s=list(s)
c=0
for i in s:
    if ord(i) in range(65,91) or ord(i) in range(97,123):
        continue
    elif ord(i)==32:
        continue
    else:
        c+=1
print(c)