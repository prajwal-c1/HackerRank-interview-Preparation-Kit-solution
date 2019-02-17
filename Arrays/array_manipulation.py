nm = input().split()

n = int(nm[0])
m = int(nm[1])

q = []
s=[0]*(n+1)


for i in range(m):
    q.append(list(map(int, input().rstrip().split())))
    x,y,incr=q[i][0],q[i][1],q[i][2]
    s[x-1] += incr
    if((y)<=len(s)): s[y] -= incr;
    
max = x = 0
for i in s:
   x=x+i;
   if(max<x): max=x;
print(max)

