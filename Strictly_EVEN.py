n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,n):
    if i%2!=0:
        if a[i]%2==0:
            print(False)
            break
else:
    print(True)