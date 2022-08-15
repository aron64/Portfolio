import numpy as np


area=np.array(
	[[0,0,0,1,1,1,2,2,2],
	 [0,0,0,1,1,1,2,2,2],
	 [0,0,0,1,1,1,2,2,2],
	 [3,3,3,4,4,4,5,5,5],
	 [3,3,3,4,4,4,5,5,5],
	 [3,3,3,4,4,4,5,5,5],
	 [6,6,6,7,7,7,8,8,8],
	 [6,6,6,7,7,7,8,8,8],
	 [6,6,6,7,7,7,8,8,8]]
)
arealocs=np.array(
	[[(0,0),(1,0),(2,0),(0,1),(1,1),(2,1),(0,2),(1,2),(2,2)],
	 [(0,3),(1,3),(2,3),(0,4),(1,4),(2,4),(0,5),(1,5),(2,5)],
	 [(0,6),(1,6),(2,6),(0,7),(1,7),(2,7),(0,8),(1,8),(2,8)],
	 [(3,0),(4,0),(5,0),(3,1),(4,1),(5,1),(3,2),(4,2),(5,2)], 
	 [(3,3),(4,3),(5,3),(3,4),(4,4),(5,4),(3,5),(4,5),(5,5)],
	 [(3,6),(4,6),(5,6),(3,7),(4,7),(5,7),(3,8),(4,8),(5,8)],
	 [(6,0),(7,0),(8,0),(6,1),(7,1),(8,1),(6,2),(7,2),(8,2)], 
	 [(6,3),(7,3),(8,3),(6,4),(7,4),(8,4),(6,5),(7,5),(8,5)],
	 [(6,6),(7,6),(8,6),(6,7),(7,7),(8,7),(6,8),(7,8),(8,8)]]
)


def areacontains(P,c):
	if c[1] in [P[x[0],x[1]] for x in arealocs[area[c[0]]]]:return True

def reject(P,c):
	if c==[]: return False
	
	if any(P[c[0][0],:]==c[1]) or any(P[:,c[0][1]]==c[1]) or areacontains(P,c):return True

def first(P,c):
	if c==[]:c=((0,0),0)
	if 0 in P[c[0][0],:]: return ((c[0][0], np.where(P[c[0][0],:]==0)[0][0]), 1)
	else:
		if c[0][0]+1<9: return ((c[0][0]+1, np.where(P[c[0][0]+1,:]==0)[0][0]), 1)

def next(P,c):
	if c[1]<9: return (c[0], c[1]+1)


def accept(P,c):
	if not 0 in P: return True

def output(P,c):
	global summa
	print(P)
	summa.append(int(str(P[0][0])+str(P[0][1])+str(P[0][2])))

def bt(c):   #P is the unsolved soduko matrix (we fill it), c is (coord(x,y), value)
    global P
    if reject(P,c):return
    if c!=[]:P[c[0][0],c[0][1]]=c[1]
    if accept(P,c):output(P,c)
    s=first(P,c)
    while s!=None:
        bt(s)
        s=next(P,s)
    if c!=[]:P[c[0][0],c[0][1]]=0


with open("p096_sudoku.txt",'r') as f:
	data=[x[:-1] for x in f.readlines()]


b=[data[x+1:x+10] for x in range(0,len(data),10)]
data=[]
for x in b:
	d1=[]
	for y in x:
		d1.append([int(z) for z in y])
	data.append(d1)

Ps=[np.array(x) for x in data]

summa=[]

for x in Ps:
	P=x
	c=[]
	bt(c)

print(summa)
print(sum(summa))