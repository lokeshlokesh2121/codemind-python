import math
n=int(input())
c=0
for i in range(0,n):
    a=int(input())
    sq=math.sqrt(a)
    for j in range(1,a):
        if sq==j:
            c=True
            break
        else:
            c=False
    print(c)