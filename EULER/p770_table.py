

n=5

N=n+1
# tet=[[0 for x in range(0,N)] for y in range(0,N)]
# profit=[[0 for x in range(0,N)] for y in range(0,N)]
# for i in range(0,N):
#     tet[0][i]=1
#     profit[i][0]=1

tet=[1 for x in range(N)]
profit=[1]+[2]*(N-1)
pnumer=[1]+[2]*(N-1)
pdenom=[1]*(N)
i=1
for i in range(1,N):
    for j in range(1,i+1):
        profit[j]=profit[j-1]+(profit[j]-profit[j-1])*profit[j-1]/(profit[j]+profit[j-1])
        pdenom[j]=pnumer[j-1]*pdenom[j]+pnumer[j]*pdenom[j-1]
        pnumer[j]=2*pnumer[j-1]*pnumer[j]
    print("PROFIT",profit)
    print("NUMER",pnumer)
    print("DENOM",pdenom)
    print("PR DIFF: ", profit[i], pnumer[i]/pdenom[i])


print(profit[N-1])


#[print(x) for x in tet]
print()

#[print(x) for x in profit]
# tet=[[1,1,1],
#    [0,0,0],
#    [0,0,0]]

# profit=[[1,2,4],
#    [1,0,0],
#    [1,0,0]]

