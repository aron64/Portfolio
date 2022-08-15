from memorize import memorize
from primes import *
@memorize()
def ways(n,i):
	if i<1:return 1
	res=0
	#k=n
	#if memo[k][i]:return memo[k][i]
	while n>=0:
		res=res+ways(n,i-1)
		n-=primes[i]
	#memo[k][i]=res
	return res

def W(n):
	N=n+1#200+1
	primes = Primes(n)
	ways=[0]*N
	ways[0]=1
	coins=primes#[ 1, 2 , 5 , 10 , 20 , 50 , 100 , 200 ]
	for i in range(len(coins)):
		#j = coins[i]
		for j in range(coins[i],N):
			ways[j]=ways[j]+ways[j-coins[i]]
	return ways[n]

n=10
while W(n)<5000:
	n+=1
print(n,W(n))
#print(ways(N,len(primes)-1))