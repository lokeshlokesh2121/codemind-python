a=int(input())
b=int(input())
c=[]
for i in range(a,b+1):
    if i>0:
        d=i
        cnt=0
        while d:
            r=d%10
            if r:
                if i%r==0:
                    cnt+=1
            d=d//10
        if len(str(i))==cnt:
            c.append(i)
print(*c)            
            