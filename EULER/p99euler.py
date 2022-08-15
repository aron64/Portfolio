with open("p099_base_exp.txt","r") as f:
	data=[tuple(int(y) for y in x[:-1].split(",")) for x in f.readlines()]


import math
log=math.log10
logged=[]
for x in data:
	logged.append(x[1]*log(x[0]))

print(logged.index(max(logged))+1)