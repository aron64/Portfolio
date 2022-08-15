# from decimal import *

# myset=[Decimal(x)**x for x in range(1,250251)]
# found=0
# for x in range(len(myset)):
# 	curr=[]
# 	if myset[x]%250==0:found+=1
# 	for y in range(x+1,len(myset))

# def subset(n):

# 	return subset()


# def d(k):
# 	return sum([int(x) for x in str(k)])

# def S(n):
# 	found=0
# 	for k in range(0,10**n,23):
# 		if k%23==0 and d(k)==23:
# 			found+=1
# 		print(k)
# 	return found

# print(6377168878570056/23)

# a=[x for x in "6578"]
# a.sort()

# b=[x for x in "8675"]
# b.sort()
# a,b=int("".join(a)),int("".join(b))

a=123
c=6
while c!=1:
	curr=[[y for y in str(a*x)] for x in range(1,7)]
	[curr[x].sort() for x in range(6)]
	curr=[int("".join(x)) for x in curr]
	c=len(set(curr))
	a+=1

print(a)
curr=[[y for y in str((a-1)*x)] for x in range(1,7)]
print(curr)
[curr[x].sort() for x in range(6)]
print(curr)
curr=[int("".join(x)) for x in curr]
print(curr)
print(set(curr))
c=len(set(curr))

#print(a==b,set([a,b]))