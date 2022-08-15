a=1
summa=0
while a<1000000:
	if bin(a)[2:]==bin(a)[2:][::-1] and str(a)==str(a)[::-1]:
		summa+=a
		print(a)
	a+=1
print(summa)