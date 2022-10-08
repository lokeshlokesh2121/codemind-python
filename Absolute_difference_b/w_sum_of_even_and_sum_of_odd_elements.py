n=int(input())
a=list(map(int,input().split()))
sum1=0
sum2=0
diff=0
for i in range(0,n):
    if a[i]%2==0:
        sum1+=a[i]
    else:
        sum2+=a[i]
diff=abs(sum2-sum1)
print(diff)