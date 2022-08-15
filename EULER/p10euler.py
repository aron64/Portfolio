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
a=[2]+[n for n in range(1,1000,2) if prime(n)]
print(a)
print(sum(a))

def taken(lista,x):
	for y in lista:
		if x%y==0:return True

def sieve(n):
	r=floor(n**0.5)
	summa=(n*(n+1))/2-1
	used=[]
	c=2
	while c<=r:
		if prime(c):
			for x in range(2,n//c+1):
				if taken(used,x):continue
				summa-=(x)*c
		used.append(c)
		c+=1
	return summa
()
print(sieve(2000000))
