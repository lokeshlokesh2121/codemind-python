n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
res=sum(a)
b=0
for i in a:
    if i>=x and i<=y:
        b+=i
print(res-b)