s=input()
k=input()
if k in "aeiouAEIOU" and k in s:
    print("True")
    print(s.index(k))
else:
    print("False")