import numpy as np

a=np.array(np.mat("""7  53 183 439 863;
497 383 563  79 973;
287  63 343 169 583;
627 343 773 959 943;
767 473 103 699 303"""))

a=np.array(np.mat("""  7  53 183 439 863 497 383 563  79 973 287  63 343 169 583;
627 343 773 959 943 767 473 103 699 303 957 703 583 639 913;
447 283 463  29  23 487 463 993 119 883 327 493 423 159 743;
217 623   3 399 853 407 103 983  89 463 290 516 212 462 350;
960 376 682 962 300 780 486 502 912 800 250 346 172 812 350;
870 456 192 162 593 473 915  45 989 873 823 965 425 329 803;
973 965 905 919 133 673 665 235 509 613 673 815 165 992 326;
322 148 972 962 286 255 941 541 265 323 925 281 601  95 973;
445 721  11 525 473  65 511 164 138 672  18 428 154 448 848;
414 456 310 312 798 104 566 520 302 248 694 976 430 392 198;
184 829 373 181 631 101 969 613 840 740 778 458 284 760 390;
821 461 843 513  17 901 711 993 293 157 274  94 192 156 574;
 34 124   4 878 450 476 712 914 838 669 875 299 823 329 699;
815 559 813 459 522 788 168 586 966 232 308 833 251 631 107;
813 883 451 509 615  77 281 613 459 205 380 274 302  35 805
"""))


# print(a)#help(np.array))
b=np.zeros((5,5), "int")
# for i in range(len(a)):
# 	for j in range(len(a[i,:])):
# 		c=a[i,j]
# 		b[i,j]=np.sum(a[i,:])+np.sum(a[:,j])
# 		print(c)

# print(b)
# for x in b:
# 	print(max(x))
# 		#print(a[i,:],a[:,i])


# def ms(mat,i,c=0):
# 	if i == -1:
# 		return 
# 	s=iter(sorted(mat[i,:],reverse=True))
# 	curr=next(s)
# 	print(np.where(mat[i,:]==curr)[0][0])

# for x in range(len(a)):
# 	ms(a,x)

a=[list(x) for x in a]
print(a)


b=[x[:] for x in a]
i=j=0
N=15
while i<N:
	j=0
	while j<N:
		a[i][j]=(a[i][j], 2**j)
		j+=1
	i+=1


a=[sorted(x, key=lambda x: -x[0]) for x in a]
print(a)

S=0
from math import *
def f(i,s,p):
	global S
	if i==N-1:
		s=s+b[i][int(log2((2**15-1)^p))]
		if s > S:
			print(s)
			S=s
		return
	j=0
	for x in a[i]:
		if(x[1]&p==0):
			j+=1
			f(i+1, s+x[0], p|x[1])
			if(j==4):break

f(0,0,0)
print(S)

#Svilen Marchev  Bulgaria   Java, ordo (n^2)*(2^n)
sol="""

public class Problem345 {
  static final int[][] mat = {
    {7, 53, 183, 439, 863, 497, 383, 563, 79, 973, 287, 63, 343, 169, 583},
    {627, 343, 773, 959, 943, 767, 473, 103, 699, 303, 957, 703, 583, 639, 913},
    {447, 283, 463, 29, 23, 487, 463, 993, 119, 883, 327, 493, 423, 159, 743},
    {217, 623, 3, 399, 853, 407, 103, 983, 89, 463, 290, 516, 212, 462, 350},
    {960, 376, 682, 962, 300, 780, 486, 502, 912, 800, 250, 346, 172, 812, 350},
    {870, 456, 192, 162, 593, 473, 915, 45, 989, 873, 823, 965, 425, 329, 803},
    {973, 965, 905, 919, 133, 673, 665, 235, 509, 613, 673, 815, 165, 992, 326},
    {322, 148, 972, 962, 286, 255, 941, 541, 265, 323, 925, 281, 601, 95, 973},
    {445, 721, 11, 525, 473, 65, 511, 164, 138, 672, 18, 428, 154, 448, 848},
    {414, 456, 310, 312, 798, 104, 566, 520, 302, 248, 694, 976, 430, 392, 198},
    {184, 829, 373, 181, 631, 101, 969, 613, 840, 740, 778, 458, 284, 760, 390},
    {821, 461, 843, 513, 17, 901, 711, 993, 293, 157, 274, 94, 192, 156, 574},
    {34, 124, 4, 878, 450, 476, 712, 914, 838, 669, 875, 299, 823, 329, 699},
    {815, 559, 813, 459, 522, 788, 168, 586, 966, 232, 308, 833, 251, 631, 107},
    {813, 883, 451, 509, 615, 77, 281, 613, 459, 205, 380, 274, 302, 35, 805},
  };

  public static void main(String[] args) {
    int n = mat.length;
    int[][] f = new int[n + 1][1 << n];
    for (int i = 0; i < n; ++i) {
      for (int b = 0; b < (1 << n); ++b) {
        for (int j = 0; j < n; ++j) {
          if (((b >> j) & 1) == 0) {
            f[i + 1][b | (1 << j)] = Math.max(f[i + 1][b | (1 << j)], f[i][b] + mat[i][j]);
          }
        }
      }
    }
    System.out.println("ans = " + f[n][(1 << n) - 1]);
  }
}"""