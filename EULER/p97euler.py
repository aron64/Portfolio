from primes import *
print(dividers(7830457))

x=0
s=1
item=1
while x!=7830457:
	x+=1
	s=s*2
	s%=10000000000
	#item=str(s)[-10:]
print(s)
print(str(int(str(s)[-10:])*28433+1)[-10:])