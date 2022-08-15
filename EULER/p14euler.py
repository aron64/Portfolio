known={}
def collatz(n):
	start=n
	steps=0
	while n!=1:
		if n in known: known=[n];break
		steps+=1
		if n%2==0:n=n/2
		else: n=3*n+1
	known[start]=steps
	steps+=1
	return steps
#print(collatz(26))
a=[collatz(x) for x in range(1,10**6)]
print(a.index(max(a)), max(a), collatz(a.index(max(a))+1))
