with open("p098_words.txt",'r') as f:
	import json
	data=json.load(f)


pairs={}
for x in data:
	s="".join(sorted(x))
	pairs[s]=pairs.get(s, [])+[x]

#print(json.dumps(pairs, indent=4))
work=[]
for x in pairs:
	if len(pairs[x])>1:
		if len(x)>3:work.append(pairs[x])

work.sort(key=lambda x:len(x[0]),reverse=True)
print(work)

curr= work[0]
last=set([x[-1] for x in curr])
print(last)
possiblelast=[1,4,6,9,5]

def passing(num, words):
	ls=[x for x in str(num)]
	print(ls)
	if len(ls)!=len(set(ls)):return False
	n2=[]
	for x in words[1]:
		n2.append(ls[words[0].index(x)])
		print(len(ls), len(words[0]),num,x,n2)
	n=int("".join(n2))
	print(n)
	print("HERE")
	if n**0.5==int(n**0.5) and n2[0]!='0':
		return (num,n)
	n2=[]
	for x in words[0]:
		n2.append(ls[words[1].index(x)])
		print(len(ls), len(words[0]),num,x,n2)
	n=int("".join(n2))
	if n**0.5==int(n**0.5) and n2[0]!='0':
		return (num,n)


x=99999
from math import *
for names in work:
	x=names[0]
	minx=(len(x)-1)
	print(minx,x)
	start=int((10**(minx+1))**0.5-1)
	print(start)
	while 2*log10(start)>=minx:
		print(x,"HERE")
		d=passing(start**2,names)#['INTRODUCE', 'REDUCTION'])
		if d:print(d);input()#;exit()
		start-=1