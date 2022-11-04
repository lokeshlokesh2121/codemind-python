n=int(input())
a=[x for x in str(n)]
for i in range(len(a)):
    if a[i]=="6":
        a[i]="9"
        break
b="".join(a)
print(b)
