#ifndef TURISTA_H
#define TURISTA_H
#include "varos.h"

class Turista
{
    public:
        static const long unsigned int kiadas;
        virtual double joSzorzo() const=0;
        virtual double kozepesSzorzo() const=0;
        virtual double lepusztultSzorzo() const=0;
        virtual int labnyom() const=0;
        virtual int labnyomTrigger() const=0;
        virtual void labnyomOverflow(int db)=0;
        virtual int getOverflow() const=0;
        virtual void setMultiplicity(int m)=0;
        virtual int getMultiplicity() const=0;
        virtual ~Turista(){}
    protected:
        Turista(){}
        int _multiplicity;
        int _overflow;

};

class Japan : public Turista
{
    public:
        virtual double joSzorzo() const override {return 1.2;}
        virtual double kozepesSzorzo() const override { return 1.0;}
        virtual double lepusztultSzorzo() const override {return 0;}
        virtual int labnyom() const override {return 0;}
        virtual int labnyomTrigger() const override {return 1;}
        virtual void labnyomOverflow(int db) override {_overflow=db;}
        virtual int getOverflow() const override {return _overflow;}
        virtual void setMultiplicity(int m) override{_multiplicity=m;}
        virtual int getMultiplicity() const override{return _multiplicity;}
        Japan(int m){_overflow=0;_multiplicity=m;}
        ~Japan(){}

};
class Modern : public Turista
{
    public:

        virtual double joSzorzo() const override {return 1.3;}
        virtual double kozepesSzorzo() const override {return 1.1;}
        virtual double lepusztultSzorzo() const override {return 1.0;}
        virtual int labnyom() const override {return -1;}
        virtual int labnyomTrigger() const override {return 100;}
        virtual void labnyomOverflow(int db) override {_overflow=db;}
        virtual int getOverflow() const override {return _overflow;}
        virtual void setMultiplicity(int m) override{_multiplicity=m;}
        virtual int getMultiplicity() const override{return _multiplicity;}
        Modern(int m){_overflow=0;_multiplicity=m;}
        ~Modern(){}

};

class KulturalisSzemetelo : public Turista
{
    public:
        virtual double joSzorzo() const override {return 1.0;}
        virtual double kozepesSzorzo() const override {return 1.1;}
        virtual double lepusztultSzorzo() const override {return 1.0;}
        virtual int labnyom() const override {return -1;}
        virtual int labnyomTrigger() const override {return 50;}
        virtual void labnyomOverflow(int db) override {_overflow=db;}
        virtual int getOverflow() const override {return _overflow;}
        virtual void setMultiplicity(int m) override{_multiplicity=m;}
        virtual int getMultiplicity() const override{return _multiplicity;}
        KulturalisSzemetelo(int m){_overflow=0;_multiplicity=m;}
        ~KulturalisSzemetelo(){}
        //static KulturalisSzemetelo* getInstance() {if(nullptr==_instance)_instance=new KulturalisSzemetelo; return _instance;}
        //~KulturalisSzemetelo()  {if(!(nullptr==_instance)) delete _instance;}
        //static KulturalisSzemetelo* _instance;
        //KulturalisSzemetelo(){_overflow=0;}
};

const long unsigned int Turista::kiadas=100000;
#endif // TURISTA_H
