products=[]
for x in range(100,10000):
	if "0" in str(x):continue
	y=1
	product=y*x
	while product<10000:
		product=x*y
		if "0" in str(y) or "0" in str(product):y+=1;continue
		ls=[int(c) for c in str(x)]+[int(c) for c in str(y)]+[int(c) for c in str(product)]
		if len(ls)!=9 or  len(set(ls))!=9:y+=1; continue
		print(x,y,product,ls, set(ls))
		products.append(product)
		y+=1

print(set(products))
c=0
for x in set(products):
	c+=x

print(c, sum(set(products)))