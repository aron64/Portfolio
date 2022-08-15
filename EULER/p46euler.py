from primes import *
ps=Primes(10000)
#print(ps)

n=3
while True:
	if n in ps: n+=2;continue
	sqn=1
	writeable=False
	while True:
		sq=sqn**2
		if 2*sq>n:break
		i=0
		while True:
			if ps[i]>n:break
			if 2*sq+ps[i]==n:
				print(ps[i],sq,n)
				writeable=True
				break
			i+=1
		if writeable:break
		sqn+=1
	if not writeable:
		print(n)
		break
	n+=2