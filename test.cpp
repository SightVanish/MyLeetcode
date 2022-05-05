#include<iostream>
#include<vector>
#include<stdlib.h>
#include<time.h>
using namespace std;

 
class A{
public:
    virtual void F() {cout << 1 << endl;}
    void callF(){F();}
    virtual ~A(){callF();F();}
};
 
class B:public A{
public:
    void F() { cout << 3 << endl;}
    void callF(){F();A::callF();}
    virtual ~B(){callF();};
};
 
int main(){
    A *p = new B();
    p->callF();
    delete p;
    system("pause");
    return 0;
}

// int main(){
//     int a=10;
//     int b=20;
//     cout<<"hello world!"<<endl;
// }