from memorize import memorize
ls={}
#@memorize()
def chain(n):
	if n==1:return 1
	if n==89:return 89
	c=sum([int(x)**2 for x in str(n)])
	if c in ls:
		return ls[c]
	ls[c]=chain(c)
	return ls[c]

f=0

for x in range(1,10**7):
	if chain(x)==89:
		f+=1
	if not f%1000:print(x,f)

print(f)

#55 50 25 29 85 89