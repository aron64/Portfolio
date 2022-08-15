from primes import *
from combinations import *
ps=permutations(4)
primes=[x for x in range(1000,10000) if prime(x)]
print(ps)
goods=[]
for x in range(len(primes)):
	base=[int(x) for x in str(primes[x])]
	basebelong=[primes[x]]
	for y in ps:
		num=[]
		for c in y:
			num.append(base[c-1])
		num=int("".join([str(x) for x in num]))
		if num in primes[x+1:]:basebelong.append(num)
	if len(set(basebelong))>=3:goods.append(set(basebelong))

lista=[]
for x in goods:
	c=list(x)
	c.sort()
	diffs=[]
	for y in range(1,len(c)):
		t=c[y]-c[y-1]
		if len(diffs):
			if t == diffs[-1]: print("AJAJ",c)
		diffs.append(t)
	#print(diffs)
# :D megtlálta de nem figyeltem, hogy a növekvő sorrendben lévő permutációnak
# nem feltétlen egymást követő tagjai lesznek a számtani sorozat elemei...
# a példa ezért ki sem jött xd
#[print(x) for x in lista]
