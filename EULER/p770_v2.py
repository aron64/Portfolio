
n=13

N=n+1

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


prev=1

#@Memoize
def hp2db(n):
    global prev
    # if(n==0):
    #     return 1
    
    prev=2*prev/hp2dn(n)
    return prev
    #return 2*hp2db(n-1)/hp2dn(n)

from math import *
i=1
x1=1
x2=0
GOAL=1.9
c=log2(2)+log2(GOAL)-log2(2-GOAL)

f1=0
f2=0
x1=c
x2=0
while x1>x2:
    f1+=log2(i)
    x1+=log2(2*i)+log2(2*i-1)
    # f1+=log2(i)
    # f2+=log2(2*i)+log2(2*i-1)
    # x1=c+f2
    x2=2*f1+(a(i)+1)+log2(hp2db(i))
    if(i%10000==0):print(i, x1-x2)
    i+=1

print(i-1)