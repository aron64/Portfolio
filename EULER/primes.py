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

def dividers(n):
	"n of divisors commented out, primes factors returned"
	divs={}
	for x in primes:
		if x**2>n:break
		while n%x==0:
			divs[x]=divs.get(x,0)+1
			n//=x
	if n!=1:
		divs[n]=divs.get(n,0)+1
	# divn=1
	# for x in divs: divn*=divs[x]+1
	return divs#,divn

primes=[2]+[n for n in range(1,100,2) if prime(n)]
def Primes(i):
	return [2]+[n for n in range(1,i+1,2) if prime(n)]

class PrimeGen():
	"""Find the next prime"""
	def __init__(self):
		self.n=1

	def next(self):
		#self.n=n
		self.n+=1
		while not prime(self.n):
			self.n+=1
		return self.n
print(prime(499))
#print(divdersi(100))
# end = 10**9

# def doIt(setin,mul):
#     s = set()
#     for y in setin:
#         z = y
#         while z <end:
#             s.add(z)
#             z*=mul
#     return s
# s= set()
# s.add(1)
# for x in p:
#     s = doIt(s,x)
# print(len(s))


N = 10**18

def nfc(num, i):
    res = 0
    p   = primes[i]
    num *= (p ** 3)
    while num <= N:
        res += N//num
        for j in range(i+1, plen):
            c = nfc(num, j)
            if c == 0: break
            res += c
        num *= p
    return res

plen = len(primes)
sol = N

for i in range(plen):
    sol += nfc(1, i)

print(sol)