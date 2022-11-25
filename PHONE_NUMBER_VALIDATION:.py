n=int(input())
if n//(10**9)==0:
    print('Invalid')
else:
    c=0
    while n!=0:
        r=n%10
        c+=1
        n//=10
    if c==10:
        print('Valid')
    else:
        print('Invalid')
        