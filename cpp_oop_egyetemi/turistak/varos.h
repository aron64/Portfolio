#ifndef VAROS_H
#define VAROS_H
#include "string.h"
#include "turista.h"
#include <iostream>

using namespace std;

class Minoseg
{
    public:
        virtual double szorzo(Turista* turista) const=0;
        virtual string megnevezes()const=0;
    protected:
        Minoseg(){}
        virtual ~Minoseg(){}
    private:

};

class Jo : public Minoseg
{
    public:

        virtual double szorzo(Turista* turista) const override {return turista->joSzorzo();}
        virtual string megnevezes() const override {return "Jo";}
        static Jo* getInstance(){if(nullptr==_instance)_instance=new Jo; return _instance;}

    protected:

    private:
        static Jo* _instance;
        Jo(){}
        ~Jo(){}
};
class Kozepes : public Minoseg
{
    public:

        virtual double szorzo(Turista* turista) const override {return turista->kozepesSzorzo();}
        virtual string megnevezes() const override {return "Kozepes";}
        static Kozepes* getInstance(){if(nullptr==_instance)_instance=new Kozepes; return _instance;}

    protected:

    private:
        static Kozepes* _instance;
        Kozepes(){}
        ~Kozepes() {}
};
class Lepusztult : public Minoseg
{

    public:

        virtual double szorzo(Turista* turista) const override {return turista->lepusztultSzorzo();}
        virtual string megnevezes() const override {return "Lepusztult";}
        static Lepusztult* getInstance(){if(nullptr==_instance)_instance=new Lepusztult; return _instance;}

    protected:

    private:
        static Lepusztult* _instance;
        Lepusztult(){}
        ~Lepusztult(){}
};


class Varos
{
    public:
        static const long long unsigned int bevetelKuszob=1000000000;
        static const long long unsigned int javitasKoltseg= 20000000;
        Varos(int pont){
            _pont=pont;
            _ideiForgalom=0;
            minosegRealizal();
        }
        void fogad(Turista* turista){
            // nem az o feladata kitalalni menniyvel jott tobb.
            // db=int(turista->multiplicity*_minoseg->szorzo(turista));
            _ideiForgalom+=turista->getMultiplicity();
            int szemeteles =(
                                (
                                    turista->getMultiplicity()+turista->getOverflow()
                                )
                                /turista->labnyomTrigger()
                            )
                            *turista->labnyom();
            turista->labnyomOverflow((turista->getMultiplicity()+turista->getOverflow()) % turista->labnyomTrigger());
            addPont(szemeteles);
        }

        void ujev(){
            //uj kenyer
            javit();
            _ideiForgalom=0;
        }
        Minoseg* getMinoseg() const{return _minoseg;}
        int getPont() const{return _pont;}
        long long unsigned int getBevetel(){return _ideiForgalom*(Turista::kiadas);}

    private:

        void minosegRealizal(){
            if(_pont<34) _minoseg=Lepusztult::getInstance();
            else if(_pont<68) _minoseg=Kozepes::getInstance();
            else _minoseg=Jo::getInstance();
        }

        void javit(){
            int tobblet = getBevetel()-Varos::bevetelKuszob;
            int pont= tobblet / (Varos::javitasKoltseg);
            if(pont>0) addPont(pont);
            minosegRealizal();
        }

        void addPont(int pont){
            _pont+=pont;
            if(_pont<1) _pont=1;
            if(_pont>100) _pont=100;
            minosegRealizal();
        }

        Minoseg* _minoseg;
        int _pont;
        long long unsigned int _ideiForgalom;
};
Jo* Jo::_instance=nullptr;
Kozepes* Kozepes::_instance=nullptr;
Lepusztult* Lepusztult::_instance=nullptr;
#endif // VAROS_H
