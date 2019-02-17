sum1=0
s=[]
ans=[]
s.append(list(map(int, input().rstrip().split())))
s.append(list(map(int, input().rstrip().split())))
s.append(list(map(int, input().rstrip().split())))
s.append(list(map(int, input().rstrip().split())))
s.append(list(map(int, input().rstrip().split())))
s.append(list(map(int, input().rstrip().split())))
#print(s[5][3])

for l in range(0,4):
    a=-1
    b=2
    for j in range(1,5):
        b+=1
        a+=1
        #print(l)
        for i in range(a,b):
            sum1+=s[l][i]+s[l+2][i]    
        sum1+=s[l+1][j]
        ans.append(sum1)
        sum1=0
        
    #print(a,b)
print(max(ans))
