n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(0,n):
    if a[i]%2==0:
        if a[i] not in l:
            l.append(a[i])
print(len(l))
 