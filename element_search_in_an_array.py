n=int(input())
a=[int(x)for x in input().split(maxsplit=n)[:n]]
b=int(input())
if b in a:
    print(True)
else:
    print(False)