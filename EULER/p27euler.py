from math import floor
def prime(n):
	if n<2: return False
	if n<4: return True
	if n%2==0: return False
	if n<9:return True
	if n%3==0: return False
	r=floor(n**0.5)
	f=5
	while f<=r:
		if n%f==0: return False
		if n%(f+2)==0: return False
		f+=6
	return True


def quadratic(a,b):
	n=0
	c=n**2+a*n+b
	while prime(c):
		n+=1
		c=n**2+a*n+b
	return n
primes=a=[2]+[n for n in range(1,1000,2) if prime(n)]
print(primes)
print(quadratic(1,41))
coef={}

for x in range(len(primes)):
	b=primes[x]
	coef[(1,b)]=quadratic(1,b)
	for y in range(0,x+1):
		a=primes[y]
		coef[(a,b)]=quadratic(a,b)
		coef[(a,-b)]=quadratic(a,-b)
		coef[(-a,-b)]=quadratic(-a,-b)
		coef[(-a,b)]=quadratic(-a,b)
		coef[(b,a)]=quadratic(b,a)
		coef[(b,-a)]=quadratic(b,-a)
		coef[(-b,-a)]=quadratic(-b,-a)
		coef[(-b,a)]=quadratic(-b,a)



print(coef)
p=lambda x: coef[x]
print(max(coef, key=p))
print(max(coef, key=p)[0]*max(coef, key=p)[1])