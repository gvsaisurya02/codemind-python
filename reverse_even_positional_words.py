s=input()
s=s.split()
r=[]
for i in s:
    if s.index(i)%2==0 or s.index(i)==0:
        r.append(i[::-1])
    else:
        r.append(i)
for i in r:
    print(i,end=" ")