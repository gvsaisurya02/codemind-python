s=input()
s=s.split()
c=0
for i in s:
    s1=i[::-1]
    s1=s1.lower()
    i=i.lower()
    if s1==i:
        c+=1
print(c)