from memorize import memorize

#@memorize()
# def ways(n,i):
# 	if i<2:return 1
# 	res=0
# 	k=n
# 	if memo[k][i]:return memo[k][i]
# 	while n>=0:
# 		res=res+ways(n,i-1)
# 		n-=i
# 	memo[k][i]=res
# 	return res

# # memo=[]
# # for x in range(N+2):
# # 	memo.append([0]*(N))

# pn=lambda n: ways(n,n-1)+1
# N=6
# memo=[]
# for x in range(N+2):
# 	memo.append([0]*(N))
# p=pn(N)
# print(p)
# exit()
# while p%(10**6)!=0:
# 	N+=1
# 	memo.append([0]*N)
# 	for x in range(N+1):
# 		memo[x].append(0)
# 	print(N)
# 	p=pn(N)

"""http://mathworld.wolfram.com/PartitionFunctionP.html"""
@memorize()
def P(n):
	"Euler-generating function"
	if n==0:return 1
	if n<0:return 0
	k=1
	res=0
	while k<=n**0.5:
		m1=n-0.5*k*(3*k-1)
		m2=n-0.5*k*(3*k+1)
		s=(-1)**(k+1)
		if m1>=0:res+=s*P(m1)
		if m2>=0:res+=s*P(m2)
		if m1<0 and m2<0:break
		#res+=(-1)**(k+1)*(P(n-0.5*k*(3*k-1))+P(n-0.5*k*(3*k+1)))
		k+=1
	return res

print(P(100))

N=5
p=P(N)
while p%(10**6):
	N+=1
	p=P(N)
	if not N%1000:print(N)

print(N,p%10**6)
