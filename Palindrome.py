n=int(input())
rev=0
t=n
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if t==rev:
    print("True")
else:
    print("False")