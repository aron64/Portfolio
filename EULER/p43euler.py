pan=[0,1,2,3,4,5,6,7,8,9]

dps={
	3:[],
	5:[],
	7:[],
	11:[],
	13:[],
	17:[]
}
twos=[]
for x in range(1000,10000):
	if x%2==0:
			p= [int(x) for x in str(x)]
			if len(p)==len(set(p)):
				twos.append(p)

for x in range(12,1000):
	for y in dps:
		if x%y==0:
			p= [int(x) for x in str(x)]
			if len(p)==2:
				p[0:0]=[0]
			if len(p)==len(set(p)):
				dps[y].append(p)

print(dps)
print(twos)
ps=[3,5,7,11,13,17]
def s(n,i):
	#if i==len(ps)-1:print("ALMOST?")
	if i==len(ps):
		print("".join(str(x) for x in n))
		return
	for x in dps[ps[i]]:
		if x[:2]==n[-2:]:
			if x[2] not in n:
				s(n+[x[2]], i+1)

for x in twos:
	#print(x)
	s(x,0)

a=[1406357289,
1430952867,
1460357289,
4106357289,
4130952867,
4160357289]
print(sum(a))