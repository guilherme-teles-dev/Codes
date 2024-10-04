/*
Descrição: Código para contar a quantidade de algarismos que compoem o número digitado n.
Entrada: Um número inteiro n;
Saída: Um número inteiro referente a quantidade de algarismos presente dentro do número n.
*/
#include <stdio.h>
int contador(int n){
    if(n < 10){
        return 1;
    }
    else{
        n = n/10;
        return 1 + contador(n);
    }
}
int main(){

    int n;
    scanf("%d", &n);

    printf("A quantidade de digitos presentes dentro do número %d é %d.\n", n, contador(n));

    return 0;
}