n=int(input())
a=list(map(int,input().split()))
tmp=0
for i in range(0,n):
    if a[i]%2==0:
        tmp=a[i]
print(tmp)        