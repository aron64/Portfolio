#inverse function of P(n)



x=0
P=lambda n: n*(3*n-1)/2
plist=[]

while 1:
	x+=1
	nextp=P(x)
	a=plist.copy()
	a.reverse()
	for y in a:
		if nextp-y in a:
			if 2*y-nextp in a:
				print(nextp, y, nextp-y)
	plist.append(nextp)




# while True:
# 	c=3*(x**2)-x+4
# 	if c%6==0:
# 		n1=P(c/6)
# 		n0=P(c/6-1)
# 		print(x-4,P(x), c/6, n1,n0,n1-n0)
# 	x+=1
# 	if x==30:break


# a=P(21)
# print(a)
# b=P(20)
# print(b)
# print(a-b)
