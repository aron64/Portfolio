c=0
for x in range(2,98633+600000):
	if sum([int(x)**5 for x in str(x)])==x:
		c+=x
		print(x)

print(c)