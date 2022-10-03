n=int(input())
n1,n2=0,1
c=0
l=[]
if n>0:
    while c<n:
        l.append(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        c+=1
if n in l:
    print("True")
else:
    print("False")