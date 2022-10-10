n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,n):
    if a[i]==0 or a[i]==1:
        c=True
    else:
        c=False
if c==True:
    print(True)
else:
    print(False)