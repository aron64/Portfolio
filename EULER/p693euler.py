from memorize import memorize

@memorize()
def l(x,y):
	a=x
	while y>1:
		y=((y%x)**2)%x
		x+=1
	res=x-a+1
	return res

@memorize()
def g(x):
	a=0;b=0;y=2
	while y<x//2+1:
	#for y in range(2,x//2+1):
		c=l(x,y)
		if c>a:a=c;b=1
		elif c==a:b+=1
		y+=1
	return a

def f(n):
	return max([g(x) for x in range(4,n+1)])

print(l(5,3))
print(f(500))
#print(f(100))
#[print(g(x),x) for x in range(3,100)]
# a=g(3)
# ls=[]
# for x in range(4,700):
# 	b=g(x)
# 	if b>a:ls.append(x)
# 	a=b
# print(ls)
# x=3000000-70000#374550+400;390550;424558-406402 -50008 -474022
# while True:
# 	print(g(x))
# 	x-=1
#print(f(100))
# [print(ls[x]-ls[x-1]) for x in range(1,len(ls))]
#print(f(5))
#print(ax)