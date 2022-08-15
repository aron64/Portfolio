a,b=1,2
s=1000
while a+b+(a**2+b**2)**0.5 !=s:
	c=(a**2+b**2)**0.5
	if b>c or a+b+c>s:
		a+=1
		b=a+1
	else:
		b+=1

print(a,b)
