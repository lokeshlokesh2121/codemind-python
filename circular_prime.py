n=int(input())
rev=(str(n)[::-1])
rev=int(rev)
for i in range(2,n):
    if n%i==0:
        break
else:
    n="prime"
for i in range(2,rev):
    if rev%i==0:
        break
else:
    rev="prime"
if(n and rev)=="prime":
    print("circular prime")
elif(n=="prime")and(rev!="prime"):
    print("prime but not a circular prime")
else:
    print("not prime")