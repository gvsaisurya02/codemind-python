a=input()
c=1
for i in range(1,len(a)):
    if ord(a[i]) in range(65,90):
        c+=1
print(c)