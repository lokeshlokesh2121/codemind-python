n=int(input())
a=[int(x)for x in input().split(maxsplit=n)[:n]]
sum=0
for i in a:
    sum+=i
tmp=sum//n
if tmp in a:
    print(True)
else:
    print(False)