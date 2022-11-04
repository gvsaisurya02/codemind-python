a=int(input())
l=[]
fa=fb=2
fn=0
for i in range(a):
    l.append(fa)
    fn=fa+fb
    fa=fb
    fb=fn
print(l[a-1])