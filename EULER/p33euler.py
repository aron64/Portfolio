ls=[]
for p in range(10,100):
	if p%10==0: continue
	for q in range(p+1,100):
		if q%10==0: continue
		for x in str(q):
			if x in str(p):
				a=[y for y in str(p)]
				b=[y for y in str(q)]
				del a[a.index(x)]
				del b[b.index(x)]
				#print(p,q)
				if int(a[0])/int(b[0])==p/q: print(p,q);ls.append((int(a[0]),int(b[0])))

print(ls)
p=1
q=1
for x in ls:
	p*=x[0]
	q*=x[1]

print(p,q)