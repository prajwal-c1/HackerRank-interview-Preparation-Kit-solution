

def top(s):
    return s[len(s)-1]


def balance(p):
    s=[]

    s.append("#")

    for i in range(len(p)):
        
        if(p[i]=="{" or p[i]=="[" or p[i]=="("):
            s.append(p[i])
        elif( p[i]==')'):
        	pop=s.pop()
        	if(pop!="("):
        		print("NO")
        		return 
        elif( p[i]==']'):
        	pop=s.pop()
        	if(pop!='['):
        		print("NO")
        		return
        elif(p[i]=='}' ):
            pop=s.pop()
            if(pop!='{'):
            	print("NO")
            	return
        
    if(top(s)=="#"):
        print("YES")
    else:
        print("NO")
            

for i in range(int(input())):
    p = input()
    result = balance(p)

        
                
