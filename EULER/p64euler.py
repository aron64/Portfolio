from math import floor
n=7
base=floor(n**0.5)
c=[1/(n**0.5-base)]
chain=[floor(c[0])]
a=0
while 1:
	k=1/(c[-1]-chain[-1])
	if len(chain)%2==0:
		if chain[:int(len(chain)/2)]==chain[int(len(chain)/2):]: break
	chain.append(floor(k))
	c.append(k)
	a+=1
	if a>50:break

print(base,chain[:int(len(chain)/2)])