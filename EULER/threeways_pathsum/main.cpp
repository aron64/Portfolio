#include <iostream>

using namespace std;

const int N=80;
int m[N][N]={0};
int oszlop[N];
int oszlop_next[N];
int main()
{
    int i,j, part_sum;
    for(i=0;i<N;++i){
        for(j=0;j<N;++j){
            cin>>m[i][j];
        }
    }

    for(i=0;i<N;++i) oszlop[i]=m[i][0];

    for(int col=1;col<N;++col){
        for(i=0;i<N;++i) oszlop_next[i]=oszlop[i]+m[i][col];

        for(i=0;i<N;++i){
            part_sum=m[i][col];
            for(j=i-1;j>=0;--j){
                part_sum+=m[j][col];
                if(part_sum>=oszlop_next[i]) break;
                if(part_sum+oszlop[j]<oszlop_next[i]) oszlop_next[i]= part_sum+oszlop[j];
            }


            part_sum=m[i][col];
            for(j=i+1;j<N;++j){
                part_sum+=m[j][col];
                if(part_sum>=oszlop_next[i]) break;
                if(part_sum+oszlop[j]<oszlop_next[i]) oszlop_next[i]= part_sum+oszlop[j];
            }
        }

        for(i=0;i<N;++i) oszlop[i]=oszlop_next[i];
    }
    int min=oszlop_next[0];
    for(i=1;i<N;++i){
        if(oszlop_next[i]<min) min=oszlop_next[i];
    } cout<<min<<endl;
    /*
    for(int i=0;i<N;++i){
        cout<<"[";
        for(int j=0;j<N;++j){
            cout<<m[i][j]<<",";
        }
        cout<<"]\n";
    }*/


    return 0;
}
