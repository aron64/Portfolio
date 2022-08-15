
def size(a,b):
	return Decimal(abs(a[0]-b[0])*abs(a[1]-b[1]))

from random import *
from decimal import *
getcontext().prec=200
f=0

def E(k):
	f=0
	for x in range(10**k):
		a=(random(), random())
		b=(random(), random())
		c=(random(), random())
		t=[size(a,b),size(a,c),size(b,c)]
		t.sort()
		f+=t[1]
	return f/10**k

print(E(8))


#print(f/10**7)