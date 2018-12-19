max=0
for i in range(5):
    a,b,c,d=map(int,input().split())
    a=a+b+c+d
    if a>max :
        max=a
        k=i
print(k+1,max)

