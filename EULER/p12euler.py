
from math import floor

def prime(n):
	if n==1: return False
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

n=1
primes=[2]+[n for n in range(1,10000,2) if prime(n)]
print(primes)

def dividers(n):
	divs={}
	for x in primes:
		while n%x==0:
			divs[x]=divs.get(x,0)+1
			n/=x
	divn=1
	for x in divs: divn*=divs[x]+1
	return divn

n=1
while 1:
	d=n*(n+1)/2
	if dividers(d)>500:
		break
	n+=1
print(n,d, dividers(d))