import math
def is_prime(x):
	u = True
	if (x%2==0 and x>2):
		return False
	for j in range(2,int(math.sqrt(x))+1,1):
		if(x%j==0):
			u = False
			break
	return u
def is_semi_prime(a):
	flag = False
	c=[]
	for i in range(2,(a//2)+1):
		if (a%i == 0 and is_prime(i)):
			c.append(i)
	#print(c,a)
	while(len(c)>0):
		temp1 = c.pop(0)
		for m in range(0,len(c)):
			if(temp1*c[m]==a):
				flag = True
				break
	c=[]
	return flag
t = int(input())
for o in range(0,t):
	a = int(input())
	flag = False
	for i in range(0,a+1):
		if(i*2==a and is_semi_prime(i)):
			flag = True
			break
		else:
			if(is_semi_prime(i) and is_semi_prime(a-i)):
				print(i)
				flag = True
				break
			
	if(flag):
		print("YES")
	else:
		print("NO")