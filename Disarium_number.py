tmp=int(input())
n=tmp
a=len(str(n))
sum=0
while n:
    r=n%10
    sum+=(r**a)
    a-=1
    n//=10
if tmp==sum:
    print(True)
else:
    print(False)