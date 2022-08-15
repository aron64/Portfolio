c=0
d=1001//2

base=[3,5,7,9]
f=[2,4,6,8]
e=1
a=1
summa=sum(base)+1
while c<d-1:
	for y in range(4):
		f[y]+=8
		base[y]+=f[y]
	summa+=sum(base)
	c+=1

print(base)
print(summa)