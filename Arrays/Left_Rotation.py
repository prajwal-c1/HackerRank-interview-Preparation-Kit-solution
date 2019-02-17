
nd = input().split()


n= int(nd[0])

r= int(nd[1])
r1=n-r

s = list(map(int, input().rstrip().split()))
#print(s)

ans=[]

for i in range(0,r1):
    ans.append(s[r+i])
    
for j in range(r):
    ans.append(s[j]) 


print(*ans)

