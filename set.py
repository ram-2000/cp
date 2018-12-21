n=int(input())
m={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
#print(type(m))
s=set()
for i in range(n):
    s.clear()
    k=input()
    for i in range(len(k)):
        s.add(k[i].lower())
    l=s.intersection(m)
    if(l==m):
        print("pangram")
    else :
        k=[]
        l=m-l
        for i in l :
            k.append(i)
        k.sort()
        print("missing",end=" ")
        for i in range(len(k)):
            print(k[i],end="")
        print()
