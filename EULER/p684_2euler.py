def power(x, y, p): 
    res = 1;
    #x = x % p;  
    while (y > 0):  
        if (y & 1): 
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

h1=lambda k:(6*( power(10,fermating(k,m),m)-1)-(k)*9) #(54*( int('1'*(k%m) )) -(k%m)*9)%m

def S2(k):
	summa=0
	he=k//9#floor(log10(k))+1
	helyi=h1(he)
	for x in range(1,k%9+1):
		#print(10**(he)+10**(he)*x-1)
		print(power(10,(he),m)+power(10,(he),m)*x-1)
		summa+=power(10,(he),m)+power(10,(he),m)*x-1
		if summa > m: 
		 	summa=summa-((summa//m)*m)
	summa+=helyi
	return summa
	