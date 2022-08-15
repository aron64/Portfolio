import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

# print(ncr(150,2))

# #2*(a*(a-1))=b*(b-1)
# a,b=1,2
# c=2*(a*(a-1))
# d=b*(b-1)
# found=[]
# while len(found)<100:
# 	a+=1
# 	c=2*(a*(a-1))
# 	d=b*(b-1)
# 	if c>d:
# 		a,b=1,b+1
# 	elif c==d:
# 		print(a,b)
# 		found.append((a,b))

# print(found)




n/p