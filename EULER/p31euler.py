coins=[1,2,5,10,20,50,100,200]
clen=len(coins)

def add(s,i):
	s+=coins[i]
	if s==200:
		return 1
	if s>200:return 0
	f=0
	for x in range(i,clen):
		c=add(s,x)
		#if c==0:break
		f+=c
	return f

res=0
for x in range(clen):
	print(x)
	res+=add(0,x)

print(res)

# 20*10
# 20*5+50*2
# 20*5+100
# 50*4
# 50*2+100
# 100*2
# 200