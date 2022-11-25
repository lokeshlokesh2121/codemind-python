
a,b=map(int,input().split())
c=(len(str(a)))-b
d=10**c
tmp=10**b
e=a//d
f=a%tmp
print(abs(e-f))

