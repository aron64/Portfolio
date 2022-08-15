import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2



def go(n,k):
    if k==2:
        print("({0} choose {1})(20 choose 20)".format(n,k),end="")
        return ncr(n,k)
    print("({0} choose {1})*(({2} choose {3})-".format(n,k,k*10, 20), end="")
    a=[go(k, i) for i in range(k-1,1,-1)]
    c=ncr(n,k)*(ncr(k*10, 20)-sum(a))
    print(")")
    return c
print(round(sum([(x*go(x))/ncr(70,20) for x in range(2,8)]),9))

#7*(1-ncr(60,20)/ncr(70,20))

exit()

from memorize import memorize
from decimal import *

@memorize()
def factorial(n):
	if n==1 or n==0:return 1
	return Decimal(n*factorial(n-1))

def nCr(n,k):
	return factorial(n)/(factorial(k)*factorial(n-k))

getcontext().prec=40
alle=nCr(70,20)
print(alle)

ml=[]
#()*(1/7)**2

twos=nCr(7,2)
print(twos/alle)
ml.append(twos/alle)
k=3
while k<=7:
	n=k*10
	favor=(nCr(7,k)* nCr(n,20)) - k*nCr(n-10,20)
	print(favor/alle)
	k+=1
	ml.append(favor/alle)

print(round(ml[1],9))#ml[1]*10**3)
print("63:",nCr(70-7,20-7)*(10**7)/alle)
cl=[]

for x in range(len(ml)):
	cl.append(ml[x]*(x+2))
	print(x+2)

print(cl)

res=0
for x in cl:
	res+=x

print(sum(cl))
print(res/6)