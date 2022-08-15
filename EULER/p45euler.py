n=1
T=lambda n: n*(n+1)/2
while 1:
	n+=1
	t=T(n)
	if n==285:
		print(n,t)
		print(((2*t+0.5)**0.5+0.5)/2)
		print(((24*t+1)**0.5+1)/6)
	if round((2*t+0.5)**0.5+0.5,2)%2==0 and ((24*t+1)**0.5+1)%6==0:
		print(t,n)