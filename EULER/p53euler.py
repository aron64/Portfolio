def factorial(n):
	if n==1 or n==0:return 1
	return n*factorial(n-1)

def nCr(n,k):
	return factorial(n)/(factorial(k)*factorial(n-k))


found=0

for n in range(1,101):
	for k in range(0,n//2+2):
		if nCr(n,k)>1000000:
			print(n,k)
			found+=len(range(k, n-k+1))
			print(found)
			break

print(found)


