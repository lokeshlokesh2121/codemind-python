n=int(input())
m=int(input())
b=m+n
a=b
while True:
    a+=1
    for i in range(2,a//2):
        if a%i==0:
            break
    else:
        print(abs(b-a))
        break