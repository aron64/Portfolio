from primes import *
print([x for x in Primes(1000000)[4:] if str(x)[0]!=str(x)[1] and
	prime(int(str(x)[:2])) and
	prime(int(str(x)[:3])) and
	prime(int(str(x)[:4])) and
	all([int(y)%2==1 and int(y)%5!=0 for y in str(x)[1:]]) and
		int(str(x)[0]) in (2,3,5,7) and int(str(x)[-2:]) in [13, 17, 23, 37, 43, 47, 53, 67, 73, 83, 97]])
print(prime(3797))
23,37,53,73
print(Primes(100))
a=[23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797,739397]
print([prime(x) for x in a])
print([prime(x) for x in (2391,299,3133,3139,1379,373)])
print(sum(a),len(a))
#[23, 37, 53, 73, 313, 317, 337, 373, 797, 3137, 3797, 5717, 5737, 7937]
c=[23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 37337, 37397, 233917, 313717, 373937, 379397, 733373, 739337, 739373, 739397]
for x in c:
	if len(str(x))>3:
		if prime(int(str(x)[1:])) and prime(int(str(x)[3:])) and prime(int(str(x)[2:])):
			print(x)
print(prime(7))