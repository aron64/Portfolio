from math import *

print(log10(4)==log10(2)+log10(2))


# 4**x-2**x=k
# x*log(4)=log(2**x+k)
# 10**(x*log(4))=10**log(2**x+k)=2**x+k
#

# x*log10(4)=x*log10(2)+log(k)
# x*log10(4)-x*log10(2)=k
# x*(log10(4)-log10(2))=k
k=6
x=log10(k)*(log10(4)-log10(2))
print(x)