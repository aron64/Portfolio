
import time
from math import ceil
from math import sqrt

start_time = time.time()


def sievePrimes(limit):
    roundUp = lambda limit, prime: int(ceil(float(limit)/prime))

    primes = [True]*limit
    primes[0] = False
    primes[1] = False

    global distFactors
    distFactors = [0]*limit


    for i in range(2,limit):
        if not primes[i]:
            global goal
            if distFactors[i] != goal:
                continue
            trigger = True
            for j in range(i + 1, i + goal):
                if distFactors[j] != goal:
                    trigger = False
                    break
            if trigger:
                return i
            else:
                continue
        distFactors[i] = 1
        for j in range(2,roundUp(limit, i)):
            primes[i*j] = False
            distFactors[i*j] += 1



maximum = 150000
distFactors = []
goal = 4
goalNum = sievePrimes(maximum)
print(goalNum)

print("--- %s seconds ---" % (time.time() - start_time))

from primes import *
known={}
def distinctn(n,consec, numdivs):
	#numdivs=[dividers(n+c)[0] for c in range(consec)]
	sets=[]
	for x in numdivs:
		if len(x)!=consec:return False
		for y in x:
			a=(y, x[y])
			if a in sets: return False
			sets.append(a)
	return True



d=dividers(14)
print(len(d[0]))
cons=4
numdivs=[dividers(10+c)[0] for c in range(cons)]
for x in range(1000,2000000-1):
	d= distinctn(x,cons, numdivs)
	if d:print(x)
	del numdivs[0]
	numdivs.append(dividers(x+cons)[0])
