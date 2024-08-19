/*
Descrição: Algoritmo para imprimir o 100 primeiros múltiplos de 3.
*/
#include <stdio.h>
void Imprime(){
    int cont = 0;
    int i = 0;
    while(cont<101){
        printf("%d\n", i);
        cont++;
        i = i+3;
    }
    printf("\n%d\n", cont);
}
int main(){
    Imprime();
}