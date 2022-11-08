n=int(input())
sum=0
for i in range(1,n+1):
    sum+=1/i
res="{:.2f}".format(sum)
print(res)