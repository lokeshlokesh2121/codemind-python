n=int(input())
a=[int(x)for x in input().split(maxsplit=n)[:n]]
sum=0
for i in a:
    sum+=i
tmp=sum/n
x=format(tmp,".2f")
print(x)