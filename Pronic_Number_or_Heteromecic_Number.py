n=int(input())
c=1
for i in range(1,n+1):
    c=i*(i+1)
    if n==c:
        break
if n==c:
    print("YES")
else:
    print("NO")