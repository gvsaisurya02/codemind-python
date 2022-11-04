s=input()
f=0
a='aeiou'
for i in a:
    if i not in s:
        f=1
        print(i,end=" ")
if f==0:
    print(0)
    