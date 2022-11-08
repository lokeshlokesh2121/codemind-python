n=int(input())
a=list(map(int,input().split()))
c=[]
for i in range(n//2,n):
    c.append(a[i])
c.reverse()
for i in range(n//2):
    c.append(a[i])
for i in range(len(c)):
    print(c[i],end=' ')