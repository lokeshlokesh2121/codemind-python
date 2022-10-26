x=int(input())
c=0
while x>0:
    rev=str(x)[::-1]
    rev=int(rev)
    c=x+rev
    rev1=str(c)[::-1]
    rev1=int(rev1)
    if c==rev1:
        print(c)
        break
    else:
        x=c