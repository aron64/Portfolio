

v2=1
n=1
d=1

from decimal import *
getcontext().prec=500
frac=1/(2+1/2)

def v2(n):
	if n==0: return Decimal(1/2)
	return Decimal(1/(2+v2(n-1)))


#print(v2f(2))
#print(v2(2))
from fractions import Fraction

print(Fraction((v2(5)+1)).limit_denominator())
print((17/12))
#[print(Fraction((v2(x)+1)).limit_denominator()) for x in range(1000)]
for x in range(1000):pass

def ex(n):
	if n%3==2:return 2*(n//3+1)
	else:return 1
ediv=[ex(n) for n in range(1,200)]
def e(en,n):
	if n==en: return Decimal(1/ediv[n])
	return Decimal(1/(ediv[n]+e(en,n+1)))

def ef(en,n):
	if n==en: return 1,ediv[n]
	nex=ef(en,n+1)
	return nex[1],ediv[n]*nex[1]+nex[0]
#	return (ediv[n]*ef(en,n+1),ef(en,n+1))
	# if n==0: return 1,2
	# c=ef(n-1)
	# d=ediv[n]*c[1]+c[0]
	# return (c[1],d)
def v2f(n):
	if n==0: return 1,2
	c=v2f(n-1)
	d=2*c[1]+c[0]
	return (c[1],d)


print("ah")
#print(ef(3,0))
nth=v2f(2-2)*2
print(nth)
denom=Decimal(nth[1])
numer=denom+nth[0]
print(numer)
print("numer",numer)
print("denom", Decimal(nth[1]))
f=0
for x in range(3,1000):
	nth=v2f(x-2)*2
	denom=Decimal(nth[1])
	numer=denom+nth[0]
	if len(str(numer))>len(str(denom)):
		f+=1
		print(numer,denom)
print(f)
def ec():
	nth=ef(6-2,0)*2
	print(nth)
	res=Decimal(nth[1])*2
	print(res)
	print("res",res+nth[0])
	print(sum([int(x) for x in str(res+nth[0])]))

#e()

# print(ediv)
#res=Fraction((2+e(100-2,0))).limit_denominator()
# print((2+e(100-2,0)))
# print(sum([int(x) for x in str(res.numerator)]))
# [print(Fraction((2+e(x-2,0))).limit_denominator()) for x in range(2,11)]
