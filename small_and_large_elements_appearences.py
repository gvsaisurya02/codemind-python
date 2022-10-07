s=input()
s=s.split()
l=[]
for i in s:
    for j in i:
        l.append(j)
mini=min(l)
maxi=max(l)
print(mini,l.count(mini),end=" ")
print(maxi,l.count(maxi))