s=input()
s=s.split(" ")
ss=0
sl=0
for i in s:
    ss+=ord(max(i))
    sl+=ord(min(i))
print(abs(ss-sl))