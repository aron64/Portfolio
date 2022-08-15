#include <iostream>
#include <string.h>
#include <fstream>
#include <vector>
using namespace std;

#include "varos.h"
#include "turista.h"


//#define NORMAL_MODE


enum ERRORS{ FILE_ERROR };

void free(vector<Turista*>&turistak){
    for(Turista* t: turistak)delete t;
}

void beolvasEv(ifstream &f, vector<Turista*>&turistak){
    int arrives[3];
    f>>arrives[0]>>arrives[1]>>arrives[2];
    for(unsigned int i=0;i<turistak.size();++i) turistak[i]->setMultiplicity(arrives[i]);
}

void sumLatogatas(vector<Turista*>&turistak, Varos* varos){
    //Parhuzamosan osszegzi a város pusztuálását, bevételét
    for(Turista* t: turistak) varos->fogad(t);
}

void sumEvek(ifstream&f, int evek, Varos* varos, vector<Turista*>&turistak){
    //ostreamre osszegzi a varos evek utani allapotat, a komplexitas miatt nehezen szurheto ki a next muvelet, de megfeleltetheto a ciklusmag eleje
    for(int i=0;i<evek;++i){
        Minoseg *m=varos->getMinoseg();
        beolvasEv(f, turistak);
        cout<<i+1<<". ev: Kezdeti pontszam: "<<varos->getPont()<<endl;
        cout<<"Tervezett:"<<"\t"<<turistak[0]->getMultiplicity()<<"\tJapan|"
                          <<"\t"<<turistak[1]->getMultiplicity()<<"\tModern|"
                          <<"\t"<<turistak[2]->getMultiplicity()<<"\tEgyeb"<<endl;
        for(Turista* t:turistak)
            t->setMultiplicity(int(t->getMultiplicity()*m->szorzo(t)));
        cout<<"Erkezett:"<<"\t"<<turistak[0]->getMultiplicity()<<"\tJapan|"
                          <<"\t"<<turistak[1]->getMultiplicity()<<"\tModern|"
                          <<"\t"<<turistak[2]->getMultiplicity()<<"\tEgyeb"<<endl<<endl;
        sumLatogatas(turistak, varos);//elvileg ez lenne a next vege

        cout<<"Eves osszesites:"<<endl
            <<"A varos a turistak latogatasa utan "<<varos->getMinoseg()->megnevezes()<<" minosegu volt."<<endl
            <<"A varos pontszama ekkor "<<varos->getPont()<<" volt."<<endl
            <<"Az eves bevetel "<<varos->getBevetel()<<" forint volt."<<endl
            <<"------------------------------------------"<<endl;

        varos->ujev();
    }
}


void simulate(const string& infile){
    ifstream f(infile);
    if(f.fail())throw FILE_ERROR;
    int kezdopont, evek;
    f>>kezdopont>>evek;
    Varos* v=new Varos(kezdopont);
    vector<Turista*> turistak;
    turistak.push_back(new Japan(0));
    turistak.push_back(new Modern(0));
    turistak.push_back(new KulturalisSzemetelo(0));
    sumEvek(f,evek,v, turistak);
    free(turistak);
}


#ifdef NORMAL_MODE

int main()
{
    try{
        simulate("input.txt");
    }catch(ERRORS err){
        cout<<"Sikertelen megnyitas";
    }

    return 0;
}

#else
#define CATCH_CONFIG_MAIN
#include "catch.hpp"

TEST_CASE("VAROS","UNIT TEST")
{
    //FOGAD, ADDPONT, MINOSEGREALIZAL, UJEV, JAVIT
    //Kelloen nagy szamokra nem mukodik
    int n=10000;
    Varos* v=new Varos(50);
    Japan* j=new Japan(n);
    v->fogad(j);
    CHECK(v->getPont()==50);
    CHECK(v->getBevetel()==Turista::kiadas*n);
    CHECK(v->getMinoseg()==Kozepes::getInstance());

    int m=2051;
    KulturalisSzemetelo* k=new KulturalisSzemetelo(m);
    v->fogad(k);
    CHECK(v->getPont()==9);//50-41
    CHECK(v->getBevetel()==Turista::kiadas*(n+m));
    CHECK(v->getMinoseg()==Lepusztult::getInstance());
    CHECK(k->getOverflow()==1);

    v->ujev();
    CHECK(v->getMinoseg()==Lepusztult::getInstance());
    CHECK(v->getPont()==19);
    CHECK(v->getBevetel()==0);

    delete v;
    delete j;
    v=new Varos(80);
    CHECK(v->getMinoseg()==Jo::getInstance());
    delete v;
}

TEST_CASE("TURISTAK","UNIT TEST")
{
    int n=100000;
    SECTION("JAPAN"){
        Japan* j=new Japan(n);
        CHECK(j->getMultiplicity()==n);
        j->setMultiplicity(0);
        CHECK(j->getMultiplicity()==0);

        CHECK(j->getOverflow()==0);
        j->labnyomOverflow(2);
        CHECK(j->getOverflow()==2);
        delete j;
    }

    SECTION("Modern"){
        Modern* m=new Modern(n);
        CHECK(m->getMultiplicity()==n);
        m->setMultiplicity(0);
        CHECK(m->getMultiplicity()==0);

        CHECK(m->getOverflow()==0);
        m->labnyomOverflow(2);
        CHECK(m->getOverflow()==2);
        delete m;
    }

    SECTION("EGYEB"){
        KulturalisSzemetelo* k=new KulturalisSzemetelo(n);
        CHECK(k->getMultiplicity()==n);
        k->setMultiplicity(0);
        CHECK(k->getMultiplicity()==0);

        CHECK(k->getOverflow()==0);
        k->labnyomOverflow(2);
        CHECK(k->getOverflow()==2);

        delete k;
    }


}

TEST_CASE("SUMEVEK, 0 ev","case1.txt")
{
    ifstream f("case1.txt");
    int kezdopont, evek;
    f>>kezdopont>>evek;
    Varos* v=new Varos(kezdopont);
    Minoseg* m=v->getMinoseg();
    vector<Turista*> turistak;
    turistak.push_back(new Japan(0));
    turistak.push_back(new Modern(0));
    turistak.push_back(new KulturalisSzemetelo(0));
    sumEvek(f,evek,v,turistak);
    CHECK(v->getPont()==kezdopont);
    CHECK(v->getBevetel()==0);
    CHECK(v->getMinoseg()==m);

    free(turistak);
}

TEST_CASE("SUMEVEK, 0 latogato","case2.txt")
{
    ifstream f("case2.txt");
    int kezdopont, evek;
    f>>kezdopont>>evek;
    Varos* v=new Varos(kezdopont);
    Minoseg* m=v->getMinoseg();
    vector<Turista*> turistak;
    turistak.push_back(new Japan(0));
    turistak.push_back(new Modern(0));
    turistak.push_back(new KulturalisSzemetelo(0));
    sumEvek(f,evek,v,turistak);
    CHECK(v->getPont()==kezdopont);
    CHECK(v->getBevetel()==0);
    CHECK(v->getMinoseg()==m);

    free(turistak);
}

TEST_CASE("SUMEVEK, 2 ev, intervallum elso elemet veszi, intervallum utolso elemet veszi","case3.txt")
{
    //kello bonyulultsagnal feltetelezhetoek a helyes kiírások, ostreamre nehéz checkelni:( ...23:24
    ifstream f("case3.txt");
    int kezdopont, evek;
    f>>kezdopont>>evek;
    Varos* v=new Varos(kezdopont);
    vector<Turista*> turistak;
    turistak.push_back(new Japan(0));
    turistak.push_back(new Modern(0));
    turistak.push_back(new KulturalisSzemetelo(0));
    sumEvek(f,evek,v, turistak);
    CHECK(v->getPont()==7);
    CHECK(v->getBevetel()==0);
    CHECK(v->getMinoseg()==Lepusztult::getInstance());

    free(turistak);
}

TEST_CASE("SUMEVEK, 1 ev, helyes vegallapot, ","case4.txt")
{

    ifstream f("case4.txt");
    int kezdopont, evek;
    f>>kezdopont>>evek;
    Varos* v=new Varos(kezdopont);
    vector<Turista*> turistak;
    turistak.push_back(new Japan(0));
    turistak.push_back(new Modern(0));
    turistak.push_back(new KulturalisSzemetelo(0));
    sumEvek(f,evek,v, turistak);
    CHECK(v->getPont()==48);
    CHECK(v->getBevetel()==0);
    CHECK(v->getMinoseg()==Kozepes::getInstance());

    free(turistak);
}


///bar probaltam parameterezni, hogy bovitheto legyen tipusokkal
///uresre nagyon nincs ertelme tesztelni, a feladat szerint 3 hosszu ugyis.
///valamit talan nem értek, ez inkább 3 összeadás mint egy összegzés, de kérték hogy iteráljunk a turistákon..
///ezreket inkább nem hoztam létre..
TEST_CASE("SUMLATOGATAS, helyes vegallapot, ","NO FILE OKAY")
{
    Varos* v=new Varos(50);
    vector<Turista*> turistak;
    turistak.push_back(new Japan(110));
    turistak.push_back(new Modern(30));
    turistak.push_back(new KulturalisSzemetelo(70));
    sumLatogatas(turistak,v);
    CHECK(v->getPont()==49);
    CHECK(v->getBevetel()==210*Turista::kiadas);
    CHECK(v->getMinoseg()==Kozepes::getInstance());
    CHECK(turistak[0]->getOverflow()==0);
    CHECK(turistak[1]->getOverflow()==30);
    CHECK(turistak[2]->getOverflow()==20);

    free(turistak);
}


#endif
