t=int(input())
for i in range(t):
    s=input()
    r=s[::-1]
    if r==s and len(s)%2==0:
        print("YES EVEN")
    elif r==s and len(s)%2!=0:
        print("YES ODD")
    else:
        print("NO")