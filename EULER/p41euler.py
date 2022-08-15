from combinations import *
from primes import *
d=permutations(6)
print(d)
for x in range(len(d)):
	n0=int("7"+"".join([str(x) for x in d[len(d)-(x+1)]]))
	if prime(n0):print(n0)

#hülyeség.. a 3-al való oszthatóság miatt legfeljebb 7jegyű lehet....