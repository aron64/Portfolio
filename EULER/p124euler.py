from primes import *
n=100000
distdivs=[False]*n
for x in range(len(distdivs)):
	c=list(dividers(x+1))
	res=1
	for y in c:
		res*=y
	distdivs[x]=res

#print(list(enumerate(distdivs)))
distrads={}
for x in range(len(distdivs)):
	rad=distdivs[x]
	distrads[rad]=distrads.get(rad, [])+[x+1]
#print(distrads)
sortedn=[]
for x in distrads:
	sortedn+=distrads[x]
#print(sortedn)
print(sortedn[10000-1])
def rad(n):pass
