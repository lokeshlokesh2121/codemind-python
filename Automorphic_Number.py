n=int(input())
sq=n*n
c=len(str(n))
res=sq%(10**c)
if res==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")