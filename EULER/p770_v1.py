

n=100000000

N=n+1
# tet=[[0 for x in range(0,N)] for y in range(0,N)]
# profit=[[0 for x in range(0,N)] for y in range(0,N)]
# for i in range(0,N):
#     tet[0][i]=1
#     profit[i][0]=1

#tet=[1 for x in range(N)]
#profit=[1]+[2]*(N-1)
#pnumer=[1]+[2]*(N-1)
#pdenom=[1]*(N)
i=1
class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        #Warning: You may wish to do a deepcopy here if returning objects
        return self.memo[args]

@Memoize
def a(n):
    if(n==0):return 0
    return a(n//2)+n


def pow2a(n):
    return 2**(a(n)+1)

@Memoize
def fact(n):
    if(n==0):return 1
    return n*(fact(n-1))

def hp2dn(n):
    return (n&(-n))

@Memoize
def hp2db(n):
    if(n==0):
        return 1
    return 2*hp2db(n-1)/hp2dn(n)

#fact(2*x)/(fact(x)^2
#[print(fact(2*x)/(fact(x)**2)) for x in range(0,15)]
#[print(pow2a(x)) for x in range(0,15)]
#aaa=[fact(x) for x in range(0,140001*2,1)]
aa=[a(x) for x in range(0,10000*2,1)]
del aa
start=10000
f1=f2=0
j=1
from math import *

while j<=start:
    f1+=log10(j)
    j+=1
f2=f1

while j<=start*2:
    f2+=log10(j)
    j+=1
print(f1, f2)
f = lambda a, b: b-a
sol=[]


for i in range(start+1,N,1):
    numer=pow2a(i)
    f1+=log10(i)
    f2+=log10(i*2)
  #  a0=10**(modf(f1)[0]+7)
  #  b=10**(modf(f2)[0]+7)
    # a0=int(a0)
    # b=int(b)
    c=f2//(f1*f1)
    c=10**(modf(c)[0]+7)
    print(c)
    exit()
    d=f(c, numer//2)
    s=int(10**floor(log10(c*2+d)))
    numer/=s
    denom=((c*2)+d)/s
    print(numer/denom)
   # print(c,d, numer, denom,s)
    print(i, numer/denom)
    sol.append(numer/denom)

print(sol)
