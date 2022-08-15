def reject(P,c):
	return False
	# for x in c: 
	# 	if c.count(x)>1: return True
def accept(P,c):
	if len(c)==P:return True
def output(P,c):
	global perms
	perms[P]=perms.get(P,[])+[c]

def first(P,c):
	for x in range(P):
		if x+1 not in c:
			return c+[x+1]

def next(P,c):
	for x in range(c[-1],P):
		if x+1 not in c:
			return c[:-1]+[x+1]

def bt(c):
    if reject(P,c):return
    if accept(P,c):output(P,c)
    s=first(P,c)
    while s!=None:
        bt(s)
        s=next(P,s)


def permutations(n):
	global perms,P
	perms={}
	P=n
	bt([])
	# return perms[n]

permutations(4)
print(perms[4],len(perms[4]))