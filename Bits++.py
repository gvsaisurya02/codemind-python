n=int(input())
l=[]
r=0
for i in range(n):
    s=input()
    l.append(s)
for i in l:
    if i=="++X" or i=="X++":
        r=r+1
    elif i=="--X" or i=="X--":
        r=r-1
    else:
        continue
print(r)


        