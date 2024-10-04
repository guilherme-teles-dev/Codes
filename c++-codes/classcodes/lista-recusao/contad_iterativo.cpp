/*
Descrição: Código para contar quantos algarismos compoem o número digitado n.
Entrada: Um número inteiro n.
Saída: Um número inteiro referente a quantidade de algarismos que compoem o número inteiro n.
*/
#include <stdio.h>
int conta_numeros(int n){
    int contador = 0;
    if(n < 10){
        return 1;
    }
    else{
        contador++;
        while(n >= 10){
            n = n/10;
            contador++;
        }
    }
    return contador;
}
int main(){

    int n;
    scanf("%d", &n);

    printf("No número %d, existem %d numeros.\n", n, conta_numeros(n));

    return 0;
}