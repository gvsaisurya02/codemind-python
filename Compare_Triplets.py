l = list(map(int,input().split()))
m = list(map(int,input().split()))
a = 0
b = 0
for i in range(0,3):
    if l[i]>m[i]:
        a+=1
    elif l[i]<m[i]:
        b+=1
    else:
        continue
print(a,b)
