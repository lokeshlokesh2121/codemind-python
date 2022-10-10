n=int(input())
a=list(map(int,input().split()))
x=int(input())
sum=0
for i in range(0,n):
    sum+=a[i]
    if a[i]==x:
        break
print(sum)