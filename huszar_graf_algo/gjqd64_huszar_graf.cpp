#include <iostream>
#include <queue>
using namespace std;

//Hertendi �ron Levente
//GJQD64

struct coord{
    int x,y;
};

int table[100][100];

int neighbors[8][2]={{1,2},
                     {1,-2},
                     {-1,2},
                     {-1,-2},
                     {2,1},
                     {2,-1},
                     {-2,1},
                     {-2,-1}}; //a husz�rl�p�s szerinti gr�fban szomsz�dos cs�csoknak a lehets�ges k�l�nbs�g vektorai a t�bl�n





int main()
{
    int n, m, x1, y1, x2, y2;


    queue<coord> Q;

    cout << "Tabla merete szokozzel elvalasztva (sorok szama, oszlopok szama)"<<endl<<"N, M: ";
    cin >>n>>m;
    cout << "Huszar koordinatai szokozzel elvalasztva"<<endl<<"i1: [1..n] , j1: [1..m] : ";
    cin >>x1>>y1;
    cout << "Cel koordinatai szokozzel elvalasztva"<<endl<<"i2: [1..n] , j2: [1..m] : ";
    cin >>x2>>y2;
    x1--;x2--;y1--;y2--;

    for(int i=0;i<n;++i)
    for(int j=0;j<m;++j)
        table[i][j]=-1; //el�g csak a sz�nek sz�mon tart�sa

    coord s;
    s.x = x1;
    s.y = y1;
    Q.push(s);
    table[s.x][s.y]=0;

    coord u,v;

    //meg akarjuk �ll�tani a sz�less�gi bej�r�st amint tal�ltunk, ekkor a table[x2][y2] v�ltozik
    // 1xN (N>1), 2xN (N>0), 3x3-as t�bl�n nem tud egy husz�r minden mez�t bej�rni, ekkor Q.empty, miel�tt a c�lmez� �rt�ke v�ltozik
    while((table[x2][y2]==-1) && !Q.empty()){
        u = Q.front(); Q.pop();
        for(int i=0;i<8;++i){
            v.x=u.x+neighbors[i][0];
            v.y=u.y+neighbors[i][1];
            if(v.x>=0 && v.x<n && v.y>=0 && v.y<m && table[v.x][v.y]==-1)
            {
                table[v.x][v.y]=table[u.x][u.y]+1;
                Q.push(v);
            }
        }
    }

    if(table[x2][y2]!=-1) cout<<"Min "<<table[x2][y2]<<" lepesben lehet eljutni."<<endl;
    else cout<<"Nem lehet eljutni"<<endl;


    cout<<"A bejaras utan a felderitett tavolsagok: "<<endl;
    for(int i=0;i<n;++i){
        for(int j=0;j<m;++j)
            cout<<table[i][j]<<" ";
        cout<<endl;
    }

    return 0;
}
