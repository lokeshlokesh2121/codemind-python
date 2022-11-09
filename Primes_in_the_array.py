n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i>1:
        for j in range(2,int(i**.5)+1):
            if i%j==0:
                break
        else:
            b.append(i)
print(len(b))