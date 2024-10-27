/*
Descrição: Programa para somar todos os números entre 1 e n recursivamente.
Entrada: Um valor inteiro n;
Saída: A soma de todos os valores entre 1 e n;
*/
//Declaração de bibliotecas que serão usadas ao longo do programa
#include <stdio.h>
//Declaração de função recursiva que irá somar os valores de 1 até n;
int sum_1_to_n(int n){
    //Declaração de uma variáveis para guardar a soma inicial, não era necessária mas achei comodo colocar mesmo assim para
    //facilitar a leitura
    int sum = 0;
    //Abertura de condicional de controle de recursividade
    if(n == 0){
        //Caso for o último termo da soma, retorne apenas ele
        return n;

    }
    //Caso ainda não for o ultimo termos, apenas some ele com o próximo termo
    else{
        sum = n+sum_1_to_n(n-1);
        return sum;

    }

    return 0;
}
//Declaração do código principal
int main(){
    //Declaração de variável responsável por guardar até que valor queremos somar
    int n;
    //Entrada do programa
    scanf("%d", &n);
    //Saída do programa;
    printf("A soma de todos os números entre 1 e %d é %d.\n", n, sum_1_to_n(n));

    return 0;
}