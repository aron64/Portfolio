from primes import *

#print(dividers(12)[0])

def rad(n,c):
	if n not in knowndiv:
		knowndiv[n]=list(dividers(n))
	distpri=knowndiv[n]
	res=1
	for x in distpri:
		res*=x
		if res>=c:return False
	return False

def gcd1(nd,md):
	# nd=list(dividers(n)[0])
	# md=list(dividers(m)[0])
	ls=nd+md
	if len(set(ls))==len(ls):
		return True
	return False
#print(rad(4320))
plittle=[n for n in range(1,100,2) if prime(n)]
#print(gcd1(32,27))
maxc=4000
abchitsc=0
knowndiv=[0]*(maxc+1)
skipc=[]
for a in range(1,maxc):
	d=1
	#print(a)
	check=0
	if a%2==0:
		d=2
	for x in plittle:
		if a%x==0:
			check=x
			break
	for b in range(a+1,maxc-a,d):
		if check:
			if b%check==0:continue
		c=a+b
		# if int(b**0.5)!=b**0.5 and int(c**0.5)!=c**0.5 and int(a**0.5)!=a**0.5:
		# 	continue
		ops=[]
		#op=[]
		found=0
		for x in [c,b,a]:
			sublist=knowndiv[x]
			if sublist==0:
				sublist=list(dividers(x))
				knowndiv[x]=sublist
			ops+=sublist
			if len(sublist)==1:
				found+=1
		if a>1 and found<1:continue
		if len(ops)==len(set(ops)):#gcd1(ops[0],ops[1]) and gcd1(ops[0],ops[2]):# and gcd1(ops[1],ops[2]):

			res=1
			dont=False
			for x in ops:
				res*=x
				if res>=c:
					dont=True
					break
			if not dont:
				# if found<1:
				# 	print(op,a,b,c)
				# if int(b**0.5)!=b**0.5 and int(c**0.5)!=c**0.5 and int(a**0.5)!=a**0.5:
				print((a,b,c))
				abchitsc+=c

res=abchitsc
print(res)#17239091
#print(sum(res))
# for x in res:
# 	for y in x:
# 		if int(y**0.5)!=y**0.5:
# 			print(x,y)
#print(sum([x[2] for x in res]))
# [(1, 8, 9), (1, 48, 49), (1, 63, 64), (1, 80, 81), (1, 224, 225),
#  (1, 288, 289), (1, 624, 625), (1, 675, 676), (1, 728, 729), 
#  (1, 960, 961), (4, 121, 125), (13, 243, 256), (25, 704, 729),
#   (32, 49, 81), (49, 576, 625), (81, 175, 256), (81, 544, 625),
#    (104, 625, 729), (200, 529, 729), (343, 625, 968)]
# [9, 49, 64, 81, 225, 243, 289, 513, 625, 676, 729, 961, 245, 128, 125, 32, 512, 250, 256, 729, 539, 81, 375, 625, 256, 625, 343, 729, 512, 729, 968]