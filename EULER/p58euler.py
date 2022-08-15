from primes import *
#primes=[2]+[x for x in range(1,5000000,2) if prime(x)]
print(primes)

def spiral():
	diff=2
	prim=0
	nums=1
	s=1
	d=0
	x=1
	while 1:
		x+=diff
		if prime(x):
			prim+=1
		nums+=1
		d+=1
		if d==4:
			d=0;diff+=2;s+=2
			a=prim/nums
			if a<0.2:
				print(prim, nums,s,a)
			if a<0.1:
				break



# n=2501
s=spiral()
# r=[(x in primes) for x in s].count(True)/len(s)

# while r>0.1:
# 	n+=2
# 	s=spiral(n)
# 	r=[(x in primes) for x in s].count(True)/len(s)
# 	print(len(s),n,r)

# print(r, s, len(s),n)

# i=0

# found=0
# while primes[i]<=c**2:
# 	found+=1
# 	i+=1
# print(found)
# print(found/(c**2))