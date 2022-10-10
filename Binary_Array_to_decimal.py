n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(0,n):
    r=a[i]*(2**n)
    sum+=r
    n-=1
res=sum//2
print(res)