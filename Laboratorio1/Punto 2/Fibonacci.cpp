#include<iostream>
#include<stdio.h>

using namespace std;

int main(){

int limite;
long double n1= 0;
long double n2= 1;

cout<<"Introduzca el n-esimo numero de la serie de Fibonnaci que desea calcular: "<<endl;
cin>>limite;

if(limite>1){
    for(int i=0;i<limite-1;i++){
        n2=n2+n1;
        n1=n2-n1;
    }
    short s = (short)n2;
    cout<<"short: "<<s<<endl;
    int i = (int)n2;
    cout<<"int: "<<i<<endl;
    long l = (long)n2;
    cout<<"long: "<<l<<endl;
    long int li = (long int)n2;
    cout<<"long int: "<<li<<endl;
    float f = (float)n2;
    cout<<"float: "<<f<<endl;
    double d = (double)n2;
    cout<<"double: "<<d<<endl;
    cout<<"long double: "<<n2<<endl;

}else if(limite==0){
    cout<<n1<<endl;
}else if(limite==1){
    cout<<n2<<endl;
}else{
    cout<<"Error, ingrese un valor mayor o igual a 0"<<endl;
}

}

/*Se calculo el n-esimo termino de la serie de Fibonacci con diferentes tipos de variables, con el fin de hallar el overflow para cada caso.
A continuación se presenta el tipo de variable junto al valor n que provoco overflow.
short 	    n=24, 	resultado = -32768
int 	    n=47, 	resultado = -2147483648
long 	    n=47, 	resultado = -2147483648
long int 	n=47, 	resultado = -2147483648
float 	    n=187,	resultado = Infinity
double  	n=1477, resultado = Infinity
long double n=23602,resultado = Infinity
 */
