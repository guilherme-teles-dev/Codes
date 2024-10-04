/*
Descrição: Programa para somar todos os números entre 1 e n recursivamente.
Entrada: Um valor inteiro n;
Saída: A soma de todos os valores entre 1 e n;
*/
#include <stdio.h>
int sum_1_to_n(int n){
    int sum = 0;
    if(n == 2){

        return n;

    }
    else{
        sum = n+sum_1_to_n(n-1);
        return sum;

    }

    return 0;
}
int main(){

    int n;
    scanf("%d", &n);

    printf("A soma de todos os números entre 1 e %d é %d.\n", n, sum_1_to_n(n-1));

    return 0;
}