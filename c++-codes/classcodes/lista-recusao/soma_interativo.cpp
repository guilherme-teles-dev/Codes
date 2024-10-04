/*
Descrição: Programa para somar todos os valores entre 1 e um valor n iterativamente.
Entrada: Um valor inteiro n qualquer.
Saída: A soma de todos os números entre 1 e n.
*/
#include <stdio.h>
int soma_one_to_n(int n){

    int soma;

    for(int c = 2; c < n; c++){
        soma = soma+c;
    }

    return soma;
}

int main(){
    int n;
    scanf("%d", &n);

    printf("A soma de todos os números entre 1 e %d é %d.\n", n, soma_one_to_n(n));

    return 0;
}