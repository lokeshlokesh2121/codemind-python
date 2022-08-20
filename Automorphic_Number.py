n=int(input())
s=n*n
a=len(str(n))
u=s%pow(10,a)
if n==u:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
    
    