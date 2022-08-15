a=1
b=2

p=a+b+(((a**2+b**2)-1)**0.5)
s=499#12499999
s=0
maxp=4000
while b<maxp/2:#250000000/2:
	a=2
	while a<=b and p<maxp:
		c=(a**2+b**2-1)**0.5
		if c==int(c):s+=1
		p=a+b+c
		a+=1
	b+=1

print(s)