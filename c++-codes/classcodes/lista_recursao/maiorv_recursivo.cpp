/*
Descrição: Código para retornar o maior elemento de um conjunto de elementos informados
Entrada: Um inteiro n que representa a quantidade de números que serão informados. Uma quantidade n de números inteiros.
Saída: O maior elementos de todos os números inteiros digitados.
*/
//Declaração das bibliotecas que serão usadas;
#include <stdio.h>
#include <stdlib.h>
//Declaração de função de criação de vetor;
int* cria_vetor(int n){
    //Declaração de ponteiro que irá receber a alocação dinâmica do vetor;
    int *vetor;
    //Alocação dinâmica do vetor;
    vetor = (int *) malloc(n*sizeof(int));
    //Abertura de looping para popular o vetor;
    for(int i = 0; i < n; i++){
        //Input de valores para o vetor;
        scanf("%d", &vetor[i]);
    }
    return vetor;
}
//Declaração de função para procurar o maior elemento do procura;
int maior_elemento(int n, int *vetor){
    //Abertura de condicional de controle de recursividade;
    if(n == 1){ //Confere se é o último elemento do vetor
        //Abertura de condicional responsável por conferir se o elemento é maior que o anterior
        if(*vetor >= *(vetor-1)){ //Se o último elemento for maior que o penultimo, retorna o último dessa comparação
            return *vetor;
        }
        else{ //Se não retorna o penultimo
            return *(vetor-1);
        }
        //A ideia dessa lógica é avançar para o último elemento do vetor e voltar comparando dois a dois até no fim sobrar apenas o maior elemento do vetor;
    }
    else{ //Enquanto não for o último elemento do vetor, chame a função recursivamente.
        return maior_elemento(n-1, vetor+1);
    }
}
//Declaração do código principal
int main(){
    //Declaração da variável que irá armazenar o tamanho do vetor e do ponteiro que será responsável por guardar o endereço do vetor alocado dinâmicamente;
    int n, *vetor;
    //Input do tamanho do vetor
    scanf("%d", &n);
    //Chamada da função que irá criar o vetor
    vetor = cria_vetor(n);
    //Output do maior elemento dos digitados;
    printf("O maior elemento foi: %d.\n", maior_elemento(n, vetor));

    return 0;
}