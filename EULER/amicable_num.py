

n=1
k=1

f=lambda k: 2**k+1
x=lambda n,k:f(k)*(2**n)-1
y=lambda n,k:f(k)*(2**(n-k))-1
z=lambda n,k:(f(k)**2)*(2**(2*n-k))-1

# a=lambda n: 2**n*x(n,k)*y(n,k)
# b=lambda n: 2**n*z(n,k)

# g=0
# for c in range(1,4):
# 	print(a(c),b(c))
# 	g+=a(c)+b(c)


# k=2
# for c in range(1,4):
# 	print(a(c),b(c))
# 	if int(a(c))==a(c) and int(b(c))==b(c):	g+=a(c)+b(c)
# k=3
# for c in range(1,4):
# 	print(a(c),b(c))
# 	if int(a(c))==a(c) and int(b(c))==b(c):	g+=a(c)+b(c)
# k=4
# for c in range(1,4):
# 	print(a(c),b(c))
# 	if int(a(c))==a(c) and int(b(c))==b(c):	g+=a(c)+b(c)




# g=0
# for k in range(1,5):
# 	for c in range(1,4):
# 		print(a(c),b(c), x(c,k), y(c,k),z(c,k))
# 		if int(a(c))==a(c) and int(b(c))==b(c):	g+=a(c)+b(c)
# 	print(str(g)+"\n")

# print(g)


def d(n):
	divs=[1]
	for x in range(2,n//2+1):
		if n%x==0:divs.append(x)
	return sum(divs)

print(d(220))
print(d(284))
amic={}
for a in range(3,10000):
	b=d(a) #=284
	if a==d(b) and a!=b:
		adding=[a,b]
		adding.sort()
		amic[adding[0]]=adding[1]

print(amic)
summa=0
for x in amic:
	summa+=x+amic[x]

print(summa)