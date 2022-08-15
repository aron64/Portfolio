# with open("p081_matrix.txt",'r') as f:
# 	data=[[int(y) for y in x[:-1].split(",")] for x in f.readlines()]

path=[]

def next(x,y):
	if data[x+1][y]>data[x][y+1]:
		next(x+1,y)
	else:
		next(x,y+1)

m="131201630537805673096803699732234342746497524103965422121037018150111956331"

ls=[int(m[x:x+3]) for x in range(0,len(m)-2,3)]
mat=[[131, 201, 630, 537, 805],
	[673, 96, 803, 699, 732],
	[234, 342, 746, 497, 524],
	[103, 965, 422, 121, 37],
	[18, 150, 111, 956, 331]]
mat1=[[131, 673, 234, 103, 18], 
[201, 96, 342, 965, 150], 
[630, 803, 746, 422, 111], 
[537, 699, 497, 121, 956],
 [805, 732, 524, 37, 331]]#[[mat[x][y] for x in range(5)] for y in range(5)]
costx=[]
costy=[]
for x in range(5):
	for y in range(5):
		if y!=4:costy.append(mat[x][y]+mat[x][y+1])
		if x!=4:costx.append(mat[x][y]+mat[x+1][y])

print(costy)
print(costx)

#GOTO file P18