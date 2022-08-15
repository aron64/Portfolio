def var(n,m):
	# 1*1-es ill. n*m-es téglalap
	#s=n*m+1
	res=0
	for x in range(n):
		for y in range(m):
			res+=(n-x)*(m-y)
	# for mi in range(m):
	# 	vertical=m-mi
	# 	s+=vertical
	# 	# if ni<n-1 and mi<m-1:
	# 	# 	s+=1
	# 	s-=1
	return res
# 2310
# print(var(425,6))
# 20351376
print(var(2000,1))

x,y=1,1

closest=[2001000,1]
while y<500:
	x+=1
	v=var(x,y)
	if abs(2000000-v)<abs(2000000-closest[0]):
		closest=[v, x*y,x,y]
		print(closest,x,y)
	if v>2000000:
		x=0
		y+=1