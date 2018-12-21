from sys import stdin
q=set()
for line in stdin :
    k=int(line)
    q.add(k%42)
print(len(q))
