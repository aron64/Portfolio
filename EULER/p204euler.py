# maxes=[]

# m={2:26, 3:16,5:11}

# b=1
# n=2**b
# while n<10**8:
# 	maxes.append(n)
# 	b+=1
# 	n=2**b

# b=1
# n=3**b
# while n<10**8:
# 	maxes.append(n)
# 	b+=1
# 	n=3**b

# b=1
# n=5**b
# while n<10**8:
# 	maxes.append(n)
# 	b+=1
# 	n=5**b

# #print(maxes, len(maxes))


# def ways(n1,n2):
# 	mx=[]
# 	b,c=1,1
# 	n=n1**b*n2**c
# 	while b<m[2]:
# 		c=1
# 		n=n1**b*n2**c
# 		while n<=10**8:
# 			mx.append(n)
# 			c+=1
# 			n=n1**b*n2**c
# 		b+=1
# 	return mx

# ls=ways(2,3)+ways(3,5)+ways(2,5)
# #print(ls,len(ls))
# def threeways(n1,n2,n3):
# 	mx=[]
# 	b,c,d=1,1,1
# 	n=n1**b*n2**c*n3**d
# 	while b<m[2]:
# 		c=1
# 		while c<m[3]:
# 			d=1
# 			n=n1**b*n2**c*n3**d
# 			while n<=10**8:
# 				mx.append(n)
# 				d+=1
# 				n=n1**b*n2**c*n3**d
# 			c+=1
# 		b+=1
# 	return mx

# def th(n1,n2,n3,b,c,d):
# 	x=n1**b*n2**c*n3**d
# 	print(x)
# 	if x>10**8: return 0
# 	return 1+th(n1, n2,n3,b+1,c,d)+th(n1, n2,n3,b,c+1,d)+th(n1, n2,n3,b,c,d+1)


# #print(len(threeways(2,3,5))+len(ls)+1+len(maxes))
# #print(th(2,3,5,1,1,1))
# # b,c=1,1
# # n=2**b*5**c
# # while b<m[2]:
# # 	n=2**b*3**c
# # 	while n<10**8:
# # 		mx.append(c)
# # 		c+=1
# # 		n=2**b*3**c
# # 	b+=1

# def reject(P,c):
# 	if expval(P,c)>10**8:
# 		return True

# def first(P,c):
# 	global i
# 	if i<len(P)-1:
# 		i+=1
# 		c[i]=0
# 		return c

# def next(P,c):
# 	global i
# 	if c[i]+1<=maxi[P[i]]:
# 		c[i]+=1
# 		return c
# def accept(P,c):
# 	if expval(P,c) not in ls:
# 		return True

# def output(P,c):
# 	ls.append(expval(P,c))
# def bt(c):
#     global i
#     if reject(P,c):return
#     if accept(P,c):output(P,c)
#     s=first(P,c)
#     while s!=None:
#         bt(s)
#         s=next(P,s)
#     i-=1


# def btx(c):
# 	for x in range(len(c)-1,-1,-1):
# 		n=expval(P,c)
# 		while n<10**8:
# 			c[x]+=1
# 			n=expval(P,c)
# 		c[x]=0
seen = set([])

def prop(n):
	global seen
	
	if n > 10**9 or n in seen: return
	seen.add(n)
	
	for i in range(1, 100):
		prop(i*n)
	

prop(1)
for i in range(1, 100+1):
	seen.add(i)

t = 0
for a in seen: t += a
print(t, len(seen))


def expval(primes,exps):
	val=1
	for x in range(len(primes)):
		val*=primes[x]**exps[x]
	return val

from primes import *
print(primes)
maxi={}
for p in primes:
	k=1
	while p**(k+1)<10**9:
		k+=1
	maxi[p]=k

i=0
ls=[]
P=primes
P=[]
print("here")
#bt([0,0,0])
#print(len(ls),ls)
ls=[]
i=len(P)-1
c=[0]*len(P)
lists=list([[x] for x in range(0,1+maxi[P[-1]])])


for y in range(2,len(P)+1):
	print(y)
	new=[]
	for x in range(0,1+maxi[P[-y]]):
		a=[]
		for y in lists:
			e=y.copy()
			e[0:0]=[x]
			a.append(e)
		for c in a:
			if expval(primes,(len(P)-len(c))*[0]+c)<=10**9:
				new.append(c)
	lists=new[:]

f=len(lists)
for x in lists:
	if expval(primes,x)>10**9:
		f-=1
print(f)
# while c[0]!=maxi[P[0]]:
# 	for d in range(len(P)-1,i,-1):
# 		c[d]
# 	for x in range(maxi[P[i]]):
# 		c[i]=x