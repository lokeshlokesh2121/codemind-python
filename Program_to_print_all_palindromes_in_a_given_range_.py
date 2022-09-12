a=int(input())
b=int(input())
for i in range(a,b+1):
    temp=i
    rev=0
    while temp>0:
        rem=temp%10
        rev=(rev*10)+rem
        temp=temp//10
    if i==rev:
        print(i,end=" ")