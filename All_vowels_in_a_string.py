s=input()
f=0
l=['a','e','i','o','u']
for i in l:
    if i not in s:
        f=1
        break
if f==1:
    print("False")
else:
    print("True")