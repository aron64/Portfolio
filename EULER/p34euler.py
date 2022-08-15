
class Memoize:

    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]

@Memoize
def f(n):
	if n<2:return 1
	if n==2:return 2
	return n*f(n-1)

fs=[f(n) for n in range(10)]
print([f(n) for n in range(10)])

def correct(n):
	s=0
	for x in str(n):
		s+=fs[int(x)]
	if s==n:return True


def r(num,i):
	if correct(num) and num>2:print(num)
	num+=fs[i]
	for j in range(i+1,10):
		r(num,j)
print(f(9)*7)
for x in range(f(9)*7):
	if correct(x):print(x)

