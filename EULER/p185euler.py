nums=[(5616185650518293,2),
(3847439647293047,1),
(5855462940810587,3),
(9742855507068353,3),
(4296849643607543,3),
(3174248439465858,1),
(4513559094146117,2),
(7890971548908067,3),
(8157356344118483,1),
(2615250744386899,2),
(8690095851526254,3),
(6375711915077050,1),
(6913859173121360,1),
(6442889055042768,2),
(2321386104303845,0),
(2326509471271448,2),
(5251583379644322,2),
(1748270476758276,3),
(4895722652190306,1),
(3041631117224635,3),
(1841236454324589,3),
(2659862637316867,2)]

a=str(2321386104303845)
b=[]
for x in nums:
	c=str(x[0])
	for y in range(len(c)):
		if c[y]==a[y]:
			c=c[:y]+"N"+c[y+1:]
	b.append((c,x[1]))

[print(x) for x in b]

bnums=[("90342" ,2),
("70794" ,0),
("39458" ,2),
("34109" ,1),
("51545" ,2),
("12531" ,1)]
bnums1=[2,0,2,1,2,1]
n=[0,0,0,0,0]
def passing(c,k):
	if len(c)==0:return True
	#k[c[-1]]=0
	print(k)
	if k==bnums1:print("HERE")
	for x in range(len(bnums)):
		# if c[-1]==bnums[x][0][len(c)-1]:
		# 	k[x]+=1
		if k[x]>bnums[x][1]: 
			#print(k,bnums[x],x)
			return False
	print("True")
	return True
def inc(c,k):
	if len(c)==0:return k
	#k[c[-1]]=0
	for x in range(len(bnums)):
		if n[k[0]]==bnums[x][0][len(c)-1]:
			k[4][x]+=1
	return k


def fits(n):
	correct={}
	for x in bnums:
		correct[x]=0
	for x in range(len(n)):
		for y in range(len(bnums)):
			if str(n[x])==bnums[y][0][x]:
				correct[bnums[y]]=correct.get(bnums[y],0)+1
				if correct[bnums[y]]>bnums[y][1]:
					#print("FALSE:",correct);
					return False
	f=0
	for y in range(len(bnums)):
		if correct[bnums[y]]==bnums[y][1]:f+=1
	if n==[3, 9, 5, 4, 2]:print(correct,bnums,f,len(bnums))
	if f==len(bnums):
		return correct


def reject(P,c):
	if c==[]:return False
	# print(c,'\n',n)
	# print(c[4])
	i= passing(n[:c[0]],c[4])
	if not i:return True
	#c=(c[0],c[1],c[2],c[3],i)
	return False

def first(P,c):
	if c==[]:
		c=(0,bnums[len(bnums)-0-1][0][0],0,[bnums[len(bnums)-0-1][0][0]],[0]*len(bnums))
		n[c[0]]=c[1]
		k=inc(n,c)
		c=(c[0],c[1],c[2],c[3],k[4])
		return c# (0,bnums[len(bnums)-0-1][0][0],0,[bnums[len(bnums)-0-1][0][0]],k[4])
	#if c[1]<9: return (c[0], c[1]+1)
	if c[0]+1<P:
		#if "2321386104303845"[c[0]+1]=="0":b=1
		c=(c[0]+1, bnums[len(bnums)-0-1][0][c[0]+1],0,[bnums[len(bnums)-0-1][0][c[0]+1]], c[4])
		n[c[0]]=c[1]
		k=inc(n,c)
		c=(c[0],c[1],c[2],c[3],k[4])
		return c#(c[0]+1, bnums[len(bnums)-0-1][0][c[0]+1],0,[bnums[len(bnums)-0-1][0][c[0]+1]], k[4])

def next(P,c):
	if c[2]<len(bnums[0][0]):
		d=1
		#if "2321386104303845"[c[0]]==str(c[1]+1):d=2
		#print(bnums[c[2]+1][0][c[0]])
		#print(c[3], len(c[3]))
		if len(c[3])==10:return
		while bnums[len(bnums)-(c[2]+d)-1][0][c[0]] in c[3]:
			d+=1
			if len(bnums)-(c[2]+d)-1<0:return
		c=(c[0], bnums[len(bnums)-(c[2]+d)-1][0][c[0]],c[2]+d, c[3]+[bnums[len(bnums)-(c[2]+d)-1][0][c[0]]],c[4])
		n[c[0]]=c[1]
		#print(n[c[0]])
		k=inc(n,c)
		#print("KKKKKKKKKKKKKKKKKKKKK:",k)
		return (c[0], bnums[len(bnums)-(c[2]+d)-1][0][c[0]],c[2]+d, c[3]+[bnums[len(bnums)-(c[2]+d)-1][0][c[0]]],k[4])

def accept(P,c):
	global n
	if c==[]:return False
	if n==[3,9,5,4,2]:print("HERE");print(fits(n),n)
	if fits(n):return True

def output(P,c):
	print("WIN",n, passing(n,c[4]));exit()

def bt(c):
    if reject(P,c):
    	if c!=[]:n[c[0]]=0
    	return
    if accept(P,c):output(P,c)
    s=first(P,c)
    while s!=None:
        bt(s)
        s=next(P,s)
    if c!=[]:n[c[0]]=0

P=5
# bnums=[]
# for x in nums:
# 	bnums.append((str(x[0]),x[1]))
n=[0]*5
bt([])

