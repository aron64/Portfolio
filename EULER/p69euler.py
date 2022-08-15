from primes import Primes

b=iter(Primes(100))

n=1
while 1:
	c=next(b)
	if n*c>10**6:break
	n*=c

print(n)