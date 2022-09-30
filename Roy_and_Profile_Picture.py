l=int(input())
N=int(input())
for i in range(N):
    w,h=map(int,input().split())
    if w<l or h<l:
        print("UPLOAD ANOTHER")
    elif w>=l and h>=l:
        if w==h:
            print("ACCEPTED")
        else:
            print("CROP IT")