s=input()
s=s.lower()
a=[]
for i in s:
    if s.count(i)==1:
        a.append(i)
a.sort()
st='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'
for i in a:
    if i==" ":
        continue
    st=st+i
print(st)