s1=input()
s2=input()
flag=0
maxs=s1
if len(s2)>len(maxs):
    maxs=s2
for i in maxs:
    if i not in s1:
        flag=1
        break
if flag==1:
    print("False")
else:
    print("True")