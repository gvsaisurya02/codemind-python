t=int(input())
for i in range(t):
    n=int(input())
    s=pow(n,1/2)
    if int(s)*int(s)==n:
        print("True")
    else:
        print("False")