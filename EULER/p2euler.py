def fib_even_sum(n,c):
	if n>4*10**6:return c
	return c+fib_even_sum(n*4+c,n)
print(fib_even_sum(2,0))