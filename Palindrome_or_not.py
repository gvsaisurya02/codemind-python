s=input()
s=s.split()
for i in s:
    s1=i[::-1]
    s1=s1.lower()
    i=i.lower()
    if s1==i:
        print("True")
    else:
        print("False")