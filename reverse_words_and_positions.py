s=input()
s=s.split()
r=[]
for i in s:
        r.append(i[::-1])
r=r[::-1]
for i in r:
    print(i,end=" ")