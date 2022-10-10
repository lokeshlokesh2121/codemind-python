n=int(input())
a=[int(x) for x in input().split(maxsplit=n)[:n]]
c=[]
for i in a:
    if i not in c:
        c.append(i)
c=sum(c)    
print(str(c))