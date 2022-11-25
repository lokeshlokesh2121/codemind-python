n=int(input())
for i in range(0,n):
    a=int(input())
    a=str(a)
    b=str(a)[::-1]
    if a==b:
        print(True)
    else:
        print(False)