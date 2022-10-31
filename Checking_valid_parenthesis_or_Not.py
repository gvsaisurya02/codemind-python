a=input()
if a.count("(")==a.count(")") or a[0]=="(" and a[len(a)-1]==")":
    print("True")
else:
    print("False")