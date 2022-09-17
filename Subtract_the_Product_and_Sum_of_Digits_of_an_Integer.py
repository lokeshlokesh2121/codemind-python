n=int(input())
s=0
t=1
while n>0:
    r=n%10
    s=s+r
    t=t*r
    n//=10
print(t-s)    
