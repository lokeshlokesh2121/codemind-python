n=int(input())
a=list(map(int,input().split()))
sum=0
c=0
for i in range(0,n):
    sum+=a[i]
avg=sum//n
for i in range(0,n):
    if a[i]>=avg:
        c+=1
print(c)        