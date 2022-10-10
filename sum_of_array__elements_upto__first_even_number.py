n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(0,n):
    if a[i]%2==0:
        break
    else:
        sum+=a[i]
print(sum)        