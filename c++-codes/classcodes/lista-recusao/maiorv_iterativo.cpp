/*
Descrição: Código para alocar um vetor dinâmicamente um vetor, popula-lo e dizer qual é o maior termo.
Entrada do programa: Os termos do vetor.
Saída do programa: O maior termos dos termos digitados.
*/
//Declaração das bibliotecas que serão usadas;
#include <stdio.h>
#include <stdlib.h>
//Declaração da função iterativa que será responsável por encontrar o maior termo do vetor.
int maior_elemento(int * vector, int n){
    //Recebe o primeiro elemento do vetor para começar comparando elemento por elemento.
    int m_elemento = vector[0];
    //Looping para percorrer o vetor comparando os elementos dele procurando o maior elemento.
    for(int i = 0; i < n; i++){
        //Abertura de condicional responsável por comparar os elementos;
        if(m_elemento < vector[i]){
            //Troca de maior elemento do vetor;
            m_elemento = vector[i];
        }
    }
    return m_elemento;
}
//Declaração de código principal
int main(){
    //Declaração de variável que irá guardar quantos elementos o vetor deve ter e de um ponteiro para receber o vetor alocado dinâmicamente.
    int n, *vector;
    //Input do tamanho do vetor;
    scanf("%d", &n);
    //Alocação dinâmica do vetor;
    vector = (int *) malloc(n*sizeof(int));
    //Abertura de looping para popular o vetor
    for(int i = 0; i < n; i++){
        scanf("%d", &vector[i]);
    }
    //Output do maior termo digitado;
    printf("O maior elemento entre os valores informados é %d.\n", maior_elemento(vector, n));

    return 0;
}