n=int(input())
a=list(map(int,input().split()))
sum1=0
sum2=0
for i in range(0,n):
    if i%2==0:
        sum1+=a[i]
    else:
        sum2+=a[i]
d=sum1-sum2
print(d)