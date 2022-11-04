s=input()
a=[]
for i in s:
    if i in "AEIOUaeiou" and i not in a:
        a.append(i)
        print(i,end=' ')