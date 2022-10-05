import math
n=int(input())
sq=math.sqrt(n)
for i in range(1,n):
    if sq==i:
        break
if sq==i:
    print(True)
else:
    print(False)