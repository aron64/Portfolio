
from decimal import *
c=[0]*7
c[-1]=3
#a=Decimal(c)**2
#print(len(str(a)))
# k=3
# while k**0.5!=int(k**0.5):
# 	c[-2]=(c[-2]+4)%10
# 	for x in range(len(c)-2,-1,-1):
# 		if c[x]==10:
# 			c[x]=0
# 			c[x-1]+=1
# 	ls=[]
# 	for x in range(7):
# 		ls.append(c[x])
# 	ls.append(0)
# 	k=int("".join([str(x) for x in ls]))
# 	print(k)
# 	# a=Decimal(c)**2
# 	# print(a)
# print(k,k**0.5)
def calc_Expectation(a, n): 
      
    # variable prb is for probability  
    # of each element which is same for 
    # each element  
    prb = 1 / n 
      
    # calculating expectation overall 
    sum = 0
    for i in range(0, n): 
        sum += (a[i] * prb)  
          
    # returning expectation as sum 
    return float(sum) 
  
  
# Driver program 
n = 3; 
a = [ 0.47,0.48,0.0001 ] 
  
# Function for calculating expectation 
expect = calc_Expectation(a, n) 
  
# Display expectation of given array 
print( "Expectation of array E(X) is : ", 
                                 expect ) 



#Powwers of two....600+
# a=0
# f=0
# for x in range(0,100000):
# 	if str(2**x)[0:3]=="123":
# 		print(x,x-a,f+1);a=x;f+=1;



# a=[(485),(485),(196),(289),(196),(289),(196),(485),(485),(196),(289),(196),(289),(196),(485),(485),(196),(289),(196),(289),(196),(485),(485),(196),(289),(196),(289),(196),(289),(196),(485),(196),(289),(196),(289),(196),(289),(196),(485),(196),(289),(196),(289),(196),(289),(196),(485),(196),(289),(196),(289),(196),(289),(196)]
# p=30
# ax=1
# n=7953
# while p!=130:
# 	n+=a[ax]
# 	ax+=1
# 	ax%=len(a)
# 	p+=1
# print(n)
# ax=2
# n=10089
# while n<678910:
# 	n+=a[ax]
# 	ax+=1
# 	ax=ax%len(a)
# 	print(ax,n)
#print(n)
exit()

c=100000000
p,k=0,0
d=Decimal(c)**2
while "123456789" not in (p,k):
	c+=10
	d=Decimal(c+3)**2
	e=Decimal(c+7)**2
	p="".join([str(d)[x] for x in range(0,len(str(d)),2)])
	k="".join([str(e)[x] for x in range(0,len(str(e)),2)])
	while int(p[1])>2:
		c+=10000;d=Decimal(c+3)**2
		p="".join([str(d)[x] for x in range(0,len(str(d)),2)])
	print(c,p,k)

print(p,k,c)
