#include <iostream>
#include <stdlib.h>

using namespace std;

int oszto_osszeg(int);
bool tokeletes(int);
bool bovelkedo(int);
bool hianyos(int);
bool baratsagos(int);
bool baratsagos_min(int a);
int beolvas_int(const string&);
int beolvas_nat(const string&);
void oszto_osszegek();
int main()
{

    cout << "Onallo feladatok!" << endl;
    int n=300;//beolvas_nat("Meddig irjam ki a szamokat:");
/*
    //Tökéletes számok kiírása n-ig
    cout<<"\nTokeletes szamok\n";
    for(int i=1; i<=n; ++i)
        if(tokeletes(i)) cout<<i<<"\t";
    cout<<endl;

    //Bõvelkedõ számok kiírása n-ig
    cout<<"\nBovelkedo szamok\n";
    for(int i=1; i<=n; ++i)
        if(bovelkedo(i)) cout<<i<<"\t";
    cout<<endl;

    //Hiányos számok kiírása n-ig
    cout<<"\nHianyos szamok\n";
    for(int i=1; i<=n; ++i)
        if(hianyos(i)) cout<<i<<"\t";
    cout<<endl;
*/
//    Barátságos számpárok kiírása n-ig
    /*cout<<"\Baratsagos szamok\n";
    for(int i=1;i<=n;++i){
        if(baratsagos_min(i)) cout<<i<<","<<oszto_osszeg(i)<<endl;
    }
    cout<<endl;*/
    oszto_osszegek();
    return 0;
}
void oszto_osszegek(){
    int N=1000000;// 1000000;
    int* t = new int[N];
    int* chains = new int[N];//kereses kozben spec ertek
    int db=0;
    for(int i=1;i<N;++i) t[i]=1;
    for(int i=2;i<=N;++i){
        for(int j=i+i;j<=N;j+=i){
            t[j-1]+=i;
        }
    }
    int k = 12504;
    int counter=-1;

    int maxhossz=0;
    int maxid=0;
    for(int i=1;i<=N;++i){
        int k=i;
        while(k<=N && k>0){
            /*/for(int i=0;i<300;++i){
                cout<<chains[i]<<" ";
            }cout<<endl;*/

            if(chains[k-1]>0){
                //chain already found, delete minus values

                break;
            }
            else if(chains[k-1]==counter){
                //here we found a number of the new chain, let's find what's in the chain
                ++db;
                int hossz=1;
                int chain_start=k;
                chains[k-1]=db;
                k=t[k-1];
                while(k!=chain_start){
                    ++hossz;
                    chains[k-1]=db;
                    k=t[k-1];
                }
                if(hossz>maxhossz){
                    maxhossz=hossz;
                    maxid=db;
                }
                break;
            }
            else{
                chains[k-1]=counter;
                k=t[k-1];
            }
        }
        --counter;
    }
    /*for(int i=0;i<N;++i){
        if(chains[i]>0) cout<<i+1<<" : "<<chains[i]<<"\n";
    }*/

    int start=0;
    while(chains[start]!=maxid) ++start;
    int min=start;
    cout<<endl<<"MINIMUM: "<<min+1<<endl;
   /* while(k<=N && k>0){
        cout<<t[k-1]<<" ";
        k=t[k-1];
    }*/
}
int beolvas_int(const string &sz){
    string s;
    bool hiba;
    int e;
    do{
        cout<<sz;
        cin>>e;
        hiba=cin.fail();
        if (hiba){
            cout<<"Ez nem egesz szam, add meg ujra!\n";
            cin.clear();  //hiba flag-ek tölése
        }
        getline(cin,s); //Enter-ig a puffer kitisztítása
        if(!hiba && s!="")
        {
            hiba=true;
            cout<<"A beirt szam utan felesleges karakterek vannak! Add meg ujra!\n";
        }
    }while (hiba);
    return e;
}

int beolvas_nat(const string &sz){
    bool hiba;
    int e;
    do{
        e=beolvas_int(sz);
        hiba=e<=0;
        if(hiba)
        {
            cout<<"Pozitiv legyen! Add meg ujra!\n";
        }
    }while(hiba);
    return e;
}

int oszto_osszeg(int k){
    int s=0;
    for(int i=1;i<=k/2;++i){
        if(k%i==0) s+=i;
    }
    return s;
}


bool tokeletes(int k){
    return k==oszto_osszeg(k);
}
bool bovelkedo(int k){
    return k<oszto_osszeg(k);
}
bool hianyos(int k){
    return k>oszto_osszeg(k);
}

// (int a)-rol megmondja hogy van e baratsagos szamparja
bool baratsagos(int a){
    int b=oszto_osszeg(a);
    if(b!=a && a==oszto_osszeg(b)) return true;
    return false;
}

//  (int a)-ra igazat ad vissza, akkor es csak akkor ha egy baratsagos szampar kisebbik tagja, igy nem irjuk ki ketszer a linearis keresesnel.
bool baratsagos_min(int a){
    int b=oszto_osszeg(a);
    if(a<b && a==oszto_osszeg(b)) return true;
    return false;
}
