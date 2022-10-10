n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,n):
    if a[i]%2!=0:
        break
else:
    c+=1
if c!=0:
    print(True)
else:
    print(False)