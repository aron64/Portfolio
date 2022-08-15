N=5
coins=(1,2,3,4,5)

class Memoize:

    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


@Memoize
def ways(s,i):
	if i<=1:print("HERE");return 1
	f=0
	while s>=0:
		print(s,i)
		f+=ways(s,i-1)
		print(s,i,f)
		s-=i
	return f

res=0
#res=ways(N,N-1)


#print(res)
