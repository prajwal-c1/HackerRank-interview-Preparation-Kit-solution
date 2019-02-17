def split2(l,n,s):
	i=l
	j=l+1
	count=0
	area=[]
	flag=0

	while i is not -1:
		if(s[l]>s[i]):
			break
		count+=1
		i-=1
	
	for j in range(l,n+1):
		flag=1
		if(s[l]>s[j]):
			break
		count+=1
	if(flag==1):
		count=count-1
	return count

def area(s,n):
	area=[]
	j=n
	
	for i in range(n):
		j-=1
		c=split2(n-i-1,n-1,s)
		area.append(c*s[j])
	print(max(area))
	

n=int(input())

s=list(map(int,input().strip().split()))
result = area(s,n)
