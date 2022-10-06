s=input()
s=s.split()
c=0
r=[]
for i in s:
    for j in i:
        if j in "aeiou":
            c+=1
    r.append(c)
    c=0
print(max(r))
    