from primes import *
from math import log10 as lg

primes=PrimeGen()
# ps=[]
# exp=[4,2,2]
# for x in range(3):
# 	ps.append(primes.next())
ps=[]
exp=[]
costs=[]
lgs=[]
nextp=primes.next()
goal=500500#2**k
a=0
while a<goal:
	l=len(exp)
	a+=1
	if not a%10**4:print(a)
	minp=nextp
	mc=lg(nextp)
	for i in range(l):
		if costs[i]<mc:
			minp=ps[i]
		if exp[i]==2:break
	if minp==nextp:
		#print(nextp)
		ps.append(nextp)
		exp+=[2]
		lgs+=[mc]
		costs+=[mc*2]
		nextp=primes.next()
	else:
		i=ps.index(minp)
		exp[i]*=2
		costs[i]=lgs[i]*exp[i]

	# res=1
	# for i in exp:res*=i

#print(ps,exp,a)
res=1
for i in range(len(exp)):
	res*=pow(ps[i],exp[i]-1, 500500507)
	res%=500500507

print(res)