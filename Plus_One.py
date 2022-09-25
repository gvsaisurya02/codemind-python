n=int(input())
l=map(int,input().split())
s=''
for i in l:
    s+=str(i)
s=int(s)+1
s=str(s)
for i in s:
    print(i,end=" ")
