n=int(input())
a=list(map(int,input().split()))
x=int(input())
c=0
for i in range(0,n):
    if a[i]==x:
        c+=1
if c!=0:
    print(c)
else:
    print("0")