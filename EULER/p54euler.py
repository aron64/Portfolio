values=['2','3','4','5','6','7','8','9','T','J','Q','K','A']
colors=['H','C','D','s']
flush_vals=['T','J','Q','K','A']
flush_vals.sort()

def royal(cards):
	vals,color=[],[]
	for x in cards:
		vals.append(x[0])
		color.append(x[1])
	vals.sort()
	print(vals,flush_vals)
	print(vals==flush_vals,len(set(color))==1)

#royal(["AH","QH", "TH","KH","JH"])

def straightflush(cards):
	vals,color=[],[]
	for x in cards:
		vals.append(values.index(x[0]))
		color.append(x[1])
	if len(set(vals))!=len(vals) or len(set(color))!=1:return 0
	vals.sort()
	if vals[0]+4==vals[-1]:
		return max(vals)
	else:return 0


def getvals(cards):
	vals={}
	for x in cards:
		v=values.index(x[0])
		vals[v]=vals.get(v,0)+1
	return vals

def foak(vals):
	if max(vals.values())==4:
		return [max(vals,key=lambda x:vals[x]),
				min(vals,key=lambda x:vals[x])]

def fullhouse(vals):
	if len(vals)==2:
		return vals

def toak(vals):
	if 3 in vals.values():
		for x in vals:
			if vals[x]==3:
				del vals[x]
				c=list(vals.keys())
				c.sort(reverse=True)
				return [x]+c

def flush(cards):
	color=[]
	for x in cards:
		color.append(x[1])
	if len(set(color))==1:return True

def straight(cards):
	vals=[]
	for x in cards:
		vals.append(values.index(x[0]))
	if len(set(vals))!=len(vals):return False
	vals.sort()
	if vals[0]+4==vals[-1]:
		return max(vals)

def twopairs(vals):
	if list(vals.values()).count(2)==2:
		one=False
		for x in vals:
			if vals[x]==1:
				del vals[x]
				c=list(vals.keys())
				c.sort(reverse=True)
				return c+[x]


def onepairs(vals):
	if 2 in list(vals.values()):
		pair=False
		for x in vals:
			if vals[x]==2:
				del vals[x]
				c=list(vals.keys())
				c.sort(reverse=True)
				return [x]+c
# print(straightflush(["AH","QH", "TH","KH","JH"]))
# print(foak_fh(["AH","AH", "AH","AH","KH"]))
# print(foak_fh(["AH","AH", "AH","KH","KH"]))

a=[[["4D", "6S", "9H", "QH", "QC",],
 	["3D", "6D", "7H", "QD", "QS",]]]

def defwinner(a,b):
	if a:
		if b:
			return a>b
		else:return True
	elif b:return False
def winner(hand1,hand2):
	a=straightflush(hand1)
	b=straightflush(hand2)
	if a or b:
		return defwinner(a,b)
	h1v=getvals(hand1)
	h2v=getvals(hand2)
	a=foak(h1v)
	b=foak(h2v)
	if a:
		if b:
			while a[0]==b[0]:
				del a[0]
				del b[0]
			return a[0]>b[0]
		else:return True
	elif b:return False
	a=fullhouse(h1v)
	b=fullhouse(h2v)
	if a:
		if b:
			a = dict((v,k) for k,v in a.items())
			b = dict((v,k) for k,v in b.items())
			if a[3]>b[3]:
				return True
			if a[3]==b[3]:
				return a[2]>b[2]
			else: return False
		else:return True
	elif b:return False

	a=flush(hand1)
	b=flush(hand2)
	if a:
		if b:
			av=list(h1v.keys())
			av.sort(reverse=True)
			bv=list(h2v.keys())
			bv.sort(reverse=True)
			while av[0]==bv[0]:
				del av[0]
				del bv[0]
			return av[0]>bv[0]
		else:return True
	elif b:return False

	a=straight(hand1)
	b=straight(hand2)
	if a or b:
		return defwinner(a,b)

	a=toak(h1v)
	b=toak(h2v)
	if a:
		if b:
			while a[0]==b[0]:
				del a[0]
				del b[0]
			return a[0]>b[0]
		else:return True
	elif b:return False

	a=twopairs(h1v)
	b=twopairs(h2v)
	if a:
		if b:
			while a[0]==b[0]:
				del a[0]
				del b[0]
			return a[0]>b[0]
		else:return True
	elif b:return False

	a=onepairs(h1v)
	b=onepairs(h2v)
	if a:
		if b:
			while a[0]==b[0]:
				del a[0]
				del b[0]
			return a[0]>b[0]
		else:return True
	elif b:return False

	a=list(h1v.keys())
	b=list(h2v.keys())
	a.sort(reverse=True)
	b.sort(reverse=True)
	while a[0]==b[0]:
		del a[0]
		del b[0]
	return a[0]>b[0]




with open("p054_poker.txt", 'r') as f:
	data=[x for x in f.read().split('\n')[:-1]]
	hands=[]
	for x in data:
		c=x.split()
		hands.append([c[:5],c[5:]])
f=0
for hand in hands:
	if winner(hand[0],hand[1]):
		f+=1

print(f)
