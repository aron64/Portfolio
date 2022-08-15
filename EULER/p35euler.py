from math import floor

def prime(n):
	if n==1: return False
	if n<4: return True
	if n%2==0: return False
	if n<9:return True
	if n%3==0: return False
	r=floor(n**0.5)
	f=5
	while f<=r:
		if n%f==0: return False
		if n%(f+2)==0: return False
		f+=6
	return True

n=1


def circles(n):
	circs=[]
	for x in range(n):
		ls=[y for y in range(x,n)]+[y for y in range(0,n-(n-x))]
		circs.append(ls)
	return circs



primes=[2]+[n for n in range(1,1000000,2) if prime(n)]
#print(perms)
perms={}
for x in range(2,7):
	perms[x]=perms.get(x,[])+circles(x)
print(perms)
found=0
for x in primes:
	prime=str(x)
	if len(prime)==1: print(prime);found+=1;continue
	if '2' in prime:continue
	if '0' in prime:continue
	if '4' in prime:continue
	if '6' in prime:continue
	if '8' in prime:continue
	iters=[]
	for x in perms[len(prime)]:
		c=""
		for y in x:
			c=c+prime[y]
		iters.append(c)
	circular=True
	for p in iters:
		if int(p) not in primes:
			circular=False
	if circular:print(prime);found+=1

print(found)

# for x in primes:
