#p40

szj=[0,9]+[9*(10**x) for x in range(1,6,1)]
szjm=[szj[x]*x for x in range(len(szj))]
szjms=[sum(szjm[:x+1]) for x in range(len(szjm))]


def d(n):
	x=0
	while n>szjms[x]: x+=1
	miotax=(n-szjms[x-1])
	xelottxjegyu=(miotax-1)//x
	szam=10**(x-1)+xelottxjegyu
	#return (n-szjms[x-1], xelottxjegyu,szam, str(szam)[(miotax-1)%x]) #//x
	return int(str(szam)[(miotax-1)%x])

from operator import mul
from functools import reduce
res=reduce(mul,[d(10**n) for n in range(0,6)],1)
print(res)