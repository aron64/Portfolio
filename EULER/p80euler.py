from decimal import *
getcontext().prec=101
v2=Decimal(2).sqrt()
[print(Decimal(x).sqrt()) for x in range(100)]
print(str(v2)[2:])
