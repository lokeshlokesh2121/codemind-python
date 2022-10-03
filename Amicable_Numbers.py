x=int(input())
y=int(input())
a=0
for i in  range(1,x):
    if x%i==0:
        a+=i
b=0
for j in range(1,y):
    if y%j==0:
        b+=j
if a==y and b==x:
    print("Amicable")
else:
    print("Not Amicable")