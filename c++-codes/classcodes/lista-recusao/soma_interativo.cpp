/*
Descrição: Programa para somar todos os valores entre 1 e um valor n iterativamente.
Entrada: Um valor inteiro n qualquer.
Saída: A soma de todos os números entre 1 e n.
*/
//Declaração das bibliotecas que serão usadas ao longo do código
#include <stdio.h>
//Declaração da função que ira realizar a soma dos valores
int soma_one_to_n(int n){
    //Declaração de variáveis responsáveis por comportar o valor da soma.
    int soma;
    //Inicialização de looping responsável por realizar a soma iterativamente;
    for(int c = 2; c < n; c++){
        soma = soma+c;
    }
    //Saída das somas realizadas
    return soma;
}
//Declaração do código principal;
int main(){
    //Declaração de variável que irá receber o valor da soma dentro da função
    int n;
    //Entrada do programa;
    scanf("%d", &n);
    //Saída da soma efetuada;
    printf("A soma de todos os números entre 1 e %d é %d.\n", n, soma_one_to_n(n));

    return 0;
}