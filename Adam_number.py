a=int(input())
sq=a*a
b=str(a)[::-1]
b=int(b)
sq2=b*b
c=str(sq2)[::-1]
sq=str(sq)
if c==sq:
    print(True)
else:
    print(False)