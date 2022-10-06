s=input()
s=s.split()
r=[]
for i in s:
    r.append(len(i))
print(min(r))