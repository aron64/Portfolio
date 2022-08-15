from memorize import memorize

# c=1000
# a=0
# for x in range(1,10):
#     a+=x*c+999
#     print(x*c+999)
# print(a)
@memorize()
def s(n):
	helyi=(10**(n//9))
	#if helyi > 1000000007: helyi=helyi-(helyi//1000000007)
	res=(n%9)*helyi+helyi-1
	return res#int(str(n%9)+'9'*(n//9))
from math import log10,floor
@memorize()
def S(k):
	summa=0
	# he=floor(log10(k))+1
	# helyi=helyisums[he]
	# for x in range(1,k%9+1):
	# 	#print(10**(he)+10**(he)*x-1)
	# 	summa+=10**(he)+10**(he)*x-1
	# summa+=helyi
	for x in range(1,k+1):
		summa+=s(x)
		# if summa > 1000000007: 
		# 	summa=summa-((summa//1000000007)*1000000007)

	# sum([s(x) for x in range(1,k+1)])
	return summa

def S1(k):
	summa=0
	he=k//9#floor(log10(k))+1
	helyi=helyisums[he]
	for x in range(1,k%9+1):
		#print(10**(he)+10**(he)*x-1)
		summa+=10**(he)+10**(he)*x-1
	summa+=helyi
	return summa
#S=lambda k: sum([s(x) for x in range(1,k+1)])

phi=(1+(5**0.5))/2
#print(S(2880067194370816120))
# print(20//9)
# print(S1(320))
# print([s(x) for x in range(82)])
# # print(2880067194370816120//9)
m=1000000007
def fermating(b,mod):
	rem=0
	b=str(b)
	print(b)
	for i in range(len(b)):
		rem = (rem*10 + ord(b[i])-48) 
		print(rem)
h=lambda k:(6*(pow(10,k%m,m)+m-1) - (k%m)*9)%m
def S2(k):
	summa=0
	he=(k)//9#floor(log10(k))+1
	if he!=k//9:print(k, he, k//9, k/9)
	if k%9==0:print(k,he)
	helyi=h(he)
	for x in range(1,k%9+1):
	   #print(10**(he)+10**(he)*x-1)
	   c=pow(10,he,m)
	   summa+=c*(x+1)-1#c+c*x-1
	   if summa > m: 
	      summa=summa-((summa//m)*m)
	summa+=helyi
	return summa
# print(fibl[-1])
#print(S(20))
fibl=[1,1]
for x in range(2,91):
	fibl.append(fibl[x-1]+fibl[x-2])
del fibl[:2]
34123259
print([h(x) for x in range(100)])
print(fibl)
print(h(4660046610375530309))
print([S(x) for x in fibl])
print(sum([S(x) for x in fibl])%m)
# 899999999108 107
# 999999999000 108
# 1999999998001 109
# 2999999997002 110
# 3999999996003 111
# 4999999995004 112
# 5999999994005 113
# 6999999993006 114
# 7999999992007 115
# 8999999991008 116
# 9999999990000 117
# 19999999980001 118
# 29999999970002 119
# 39999999960003 120
# 49999999950004 121
# 59999999940005 122