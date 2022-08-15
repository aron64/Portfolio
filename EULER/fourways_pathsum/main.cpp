#include <iostream>

using namespace std;
int min(int &a, int &b){return a<b?a:b;}
const int N=80;
int m[N][N]={0};
int cost[N][N]={0};

void two_ways(int a, int b){
    for(int j=b;j<N;++j){
        for(int i=a;i<N;++i){
            if(i==0 && j==0)continue;
            if(j==0) cost[i][j]=m[i][j]+cost[i-1][0];
            else if(i==0) cost[i][j]=m[i][j]+cost[0][j-1];
            else cost[i][j]=m[i][j]+min(cost[i-1][j],cost[i][j-1]);
        }
    }
}

int main()
{
    int i,j, part_sum;
    for(i=0;i<N;++i){
        for(j=0;j<N;++j){
            cin>>m[i][j];
        }
    }
    cout<<endl;
    cost[0][0]=m[0][0];
    two_ways(0,0);
    /*for(i=0;i<N;++i){
        for(j=0;j<N;++j){
            cout<<cost[i][j]<<" ";
        }cout<<endl;
    }cout<<endl;cout<<endl;*/

        /*
    for(j=0;j<N;++j){
        for(i=0;i<N;++i){
            if(i==0 && j==0)continue;
            if(j==0) cost[i][j]=m[i][j]+cost[i-1][0];
            else if(i==0) cost[i][j]=m[i][j]+cost[0][j-1];
            else cost[i][j]=m[i][j]+min(cost[i-1][j],cost[i][j-1]);
        }
    }*/
    //for(i=N-1; i>=0; --i)
    //for(j=N-1; j>=0; --j)
    bool change=false;
    do{
            change=false;
    for(i=0;i<N;++i){
        for(j=0;j<N;++j){
            if(i<N-1 && cost[i+1][j]+m[i][j]<cost[i][j]){
                change=true;
                cost[i][j]=cost[i+1][j]+m[i][j];
                two_ways(i,j+1);
            }
        }
    }

    for(j=0;j<N;++j){
        for(i=0;i<N;++i){
            if(j<N-1 && cost[i][j+1]+m[i][j]<cost[i][j]){
                change=true;
                cost[i][j]=cost[i][j+1]+m[i][j];
                two_ways(i+1,j);
            }
        }
    }
    }while(change==true);
   /* for(i=0;i<N;++i){
        for(j=0;j<N;++j){
            cout<<cost[i][j]<<" ";
        }cout<<endl;
    }*/
    cout << cost[N-1][N-1] << endl;
    return 0;
}
