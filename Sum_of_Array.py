n=int(input())
a=[int(x)for x in input().split(maxsplit=n)[:n]]
s=0
for i in a:
    s+=i
print(s)    