s=input()
s=s.split(" ")
s=s[-1]
s=list(s)
m=min(s)
if m.lower() in s:
    print(m.lower())
else:
    print(m)