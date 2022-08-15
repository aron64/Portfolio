

n=12607

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

[print(hp2db(n)) for n in range(0,15)]
#fact(2*x)/(fact(x)^2
#[print(fact(2*x)/(fact(x)**2)) for x in range(0,15)]
#[print(pow2a(x)) for x in range(0,15)]
#aaa=[fact(x) for x in range(0,140001*2,1)]
aa=[a(x) for x in range(0,10000*2,1)]
del aa
start=1
f1=f2=1
j=2
from math import *
f1=factorial(start)
print("HI")
f2=factorial(start*2)
print("HI")
# print("here")
# while j<=start:
#     f1=j*f1
#     j+=1
# f2=f1

# while(f2&1==0):
#     print("HERE",f2)
#   #  f2//=2
# while j<=start*2:
#     p=j
#     print("HERE")
#     while(p%2==0):p//=2
#     f2=p*f2
#     j+=1
# print(f1, f2)
f = lambda a, b: b-a
sol=[]
for i in range(start+1,N,1):
    numer=pow2a(i)
    f1=f1*i
 #   print(f2, i*2, (i*2)-1)
    f2=f2*(i*2)*((i*2)-1)
    print("HI", f2, f1)
    
    c=f2//(f1*f1)
    #c=fact(2*i)//(fact(i)**2)
    print("count", hp2db(i), log2(numer//2), c)
    c=c/hp2db(i)
    d=f(c, numer//2)
    #print(c,f,numer,d)
    s=int(10**floor(log10(c*2+d)))
   # numer/=s
    denom=((c*2)+d)
   # print(c,d, numer, denom,s)
    print(i, numer/denom)
    sol.append(numer/denom)

print(sol)
exit()
for i in range(1,N):
    for j in range(1,i+1):
        profit[j]=profit[j-1]+(profit[j]-profit[j-1])*profit[j-1]/(profit[j]+profit[j-1])
        profit[j]=round(profit[j],5)
        pdenom[j]=pnumer[j-1]*pdenom[j]+pnumer[j]*pdenom[j-1]
        pnumer[j]=2*pnumer[j-1]*pnumer[j]
        while(pdenom[j]%2==0):
            pdenom[j]//=2
            pnumer[j]//=2
    if j%1==0:
        print("--------", j, "----------")
        print("PROFIT",profit)
        print("NUMER",pnumer)
        print("DENOM",pdenom)
        print("PR DIFF: ", profit[i], pnumer[i]/pdenom[i])


print(profit[N-1])


#[print(x) for x in tet]
print()

#[print(x) for x in profit]
# tet=[[1,1,1],
#    [0,0,0],
#    [0,0,0]]

# profit=[[1,2,4],
#    [1,0,0],
#    [1,0,0]]