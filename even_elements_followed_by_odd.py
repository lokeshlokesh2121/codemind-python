n=int(input())
a=list(map(int,input().split()))
c=[]
d=[]
e=[]
for i in a:
    if i%2==0:
        c.append(i)
    else:
        d.append(i)
for i in c:
    e.append(i)
for i in d:
    e.append(i)
print(*e)