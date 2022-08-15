
def lychrel(n,c):
	s=str(n)
	if s==s[::-1] and c>0:return False
	if c>=50:return True
	else: return lychrel(n+int(s[::-1]),c+1)

print([lychrel(x,0) for x in range(0,10000)].count(True))
print(lychrel(4994,0))