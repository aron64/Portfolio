td="""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
triangle = td.split("\n")
triangle=[[int(y) for y in x.split()] for x in triangle]
print(triangle)

# d=[triangle[-1].copy()]
# for x in range(len(triangle)-2,-1,-1):
# 	c=[]
# 	for y in range(len(triangle[x])):
# 		c.append(triangle[x+1][y]+triangle[x+1][y+1]+triangle[x][y])
# 		#c.append(d[0][y]+d[0][y+1]+triangle[x][y])   #+triangle[x][y]
# 	d[0:0]=[c]

# print(d)

# path=[0]
# for x in range(len(d)-1):
# 	if d[x+1][path[-1]]>d[x+1][path[-1]+1]:path.append(path[-1])
# 	else:path.append(path[-1]+1)

# print(path)
# print([triangle[x][path[x]] for x in range(len(triangle))])
# print(sum([triangle[x][path[x]] for x in range(len(triangle))]))
# print(sum([triangle[x][0] for x in range(len(triangle))]))

#######################################################################P64

# with open("p067_triangle.txt",'r') as f:
# 	data=f.read(3122312)
# 	print(data)
# 	triangle = data.split("\n")[:-1]
# 	triangle=[[int(y) for y in x.split()] for x in triangle]
# 	print(triangle)
# d=triangle.copy()
# for x in range(1,len(d)):
# 	d[x][0]+=d[x-1][0]
# 	d[x][-1]+=d[x-1][-1]
# 	for y in range(1,len(d[x])-1):
# 		d[x][y]+= max(d[x-1][y-1], d[x-1][y])
# 		# d[x+1][y]+=d[x][y]
# 		# d[x+1][y+1]+=d[x][y]

# print(d)

# print(max(d[-1]))

############################################################################

# for x in range(len(d)-1,0,-1):
# 	if d[x][path[-1]]>d[x][path[-1]-1]:path.append(path[-1])
# 	else:path.append(path[-1]-1)

# print(path)
# print(len(path),len(d),len(triangle))
# path.reverse()
# triangle = td.split("\n")
# triangle=[[int(y) for y in x.split()] for x in triangle]
# print([triangle[x][path[x]] for x in range(len(triangle))])
# print(sum([triangle[x][path[x]] for x in range(len(triangle))]))
# print(sum([triangle[x][0] for x in range(len(triangle))]))
mat1=[[131, 201, 630, 537, 805],
	[673, 96, 803, 699, 732],
	[234, 342, 746, 497, 524],
	[103, 965, 422, 121, 37],
	[18, 150, 111, 956, 331]]
mat=[[131, 673, 234, 103, 18], 
[201, 96, 342, 965, 150], 
[630, 803, 746, 422, 111], 
[537, 699, 497, 121, 956],
 [805, 732, 524, 37, 331]]
with open("p081_matrix.txt",'r') as f:
	data=f.read()
	data = data.split("\n")[:-1]
	data=[[int(y) for y in x.split(",")] for x in data]
#mat=data
sorok=len(mat)+len(mat[0])-1
triangle=[[0]*x for x in range(1,sorok+1)]
for x in range(sorok):
	a,b=x,0
	while a!=-1:
		try:
			triangle[x][b]=mat[a][b]
		except:
			triangle[x][b]=0
		a-=1
		b+=1
[print(x) for x in triangle]

print(triangle)

d=triangle.copy()
for x in range(1,len(d)):
	d[x][0]+=d[x-1][0]
	d[x][-1]+=d[x-1][-1]
	for y in range(1,len(d[x])-1):
		d[x][y]+= min(d[x-1][y-1], d[x-1][y])
		# d[x+1][y]+=d[x][y]
		# d[x+1][y+1]+=d[x][y]

print(d)

print(max(d[-1]))