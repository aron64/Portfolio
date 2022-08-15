

N=11
tet=[[0 for x in range(0,N)] for y in range(0,N)]
profit=[[0 for x in range(0,N)] for y in range(0,N)]
for i in range(0,N):
    for j in range(0,N):
        if(i==0):
            tet[i][j]=1
            profit[i][j]=2**j
        else:
            tet[i][j]==0
        if(j==0):
            profit[i][j]=1



i=1
for i in range(1,N):
    for j in range(1,N):
        tet[i][j]=(profit[i-1][j]-profit[i][j-1])/(profit[i-1][j]+profit[i][j-1])
        profit[i][j]=(1+tet[i][j])*profit[i][j-1]
        if(i==j):print(profit[i][j], tet[i][j])


print(profit[N-1][N-1])


[print(x) for x in tet]
print()

[print(x) for x in profit]
# tet=[[1,1,1],
#    [0,0,0],
#    [0,0,0]]

# profit=[[1,2,4],
#    [1,0,0],
#    [1,0,0]]