n=int(input())
a=list(map(int,input().split()))
c=[]
if n%2!=0:
    a.append(0)
for i in range(len(a)):
    c.append(a[i])
    print(c[i],end=' ')