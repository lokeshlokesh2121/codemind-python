n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
l=[]
for i in range(0,n):
    if a[i]>=x and a[i]<=y:
        l.append(a[i])
if len(l)==0:
    print(-1)
else:
    print(min(l))
 