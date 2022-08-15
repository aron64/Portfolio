from primes import *

ps=Primes(1000000)
print(ps)


def primesum(n,i,c):
	if n in ps and c>1:
		print(n,c)
	if n>10**6:
		return
	primesum(n+ps[i+1],i+1,c+1)

for x in range(len(ps)):
	primesum(0,x,0)
	break # :D
# 1987 19
# 2647 23
# 3391 27
# 5641 37
# 6701 41