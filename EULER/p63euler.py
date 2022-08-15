from decimal import *
getcontext().prec=200
print(len(str(Decimal(9)**21)))
found=0
b=1
while b<22:
	a=1
	num=Decimal(a)**b
	digits=len(str(num))
	while digits<=b:
		if digits==b:
			print(a,b, num,digits)
			found+=1
		a+=1
		num=Decimal(a)**b
		digits=len(str(num))
	b+=1
print(found)