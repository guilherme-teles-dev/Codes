/*
Descrição: Código para retornar o maior elemento de um conjunto de elementos informados
Entrada: Um inteiro n que representa a quantidade de números que serão informados. Uma quantidade n de números inteiros.
Saída: O maior elementos de todos os números inteiros digitados.
*/
#include <stdio.h>
#include <stdlib.h>
int* cria_vetor(int n){
    int *vetor;
    vetor = (int *) malloc(n*sizeof(int));
    for(int i = 0; i < n; i++){
        scanf("%d", &vetor[i]);
    }
    return vetor;
}
int maior_elemento(int n, int *vetor){
    if(n == 1){
    if(*vetor >= *(vetor-1)){
            return *vetor;
        }
        else{
            return *(vetor-1);
        }
    }
    else{
        return maior_elemento(n-1, vetor+1);
    }
}
int main(){

    int n, *vetor;
    scanf("%d", &n);
    vetor = cria_vetor(n);
    printf("O maior elemento foi: %d.\n", maior_elemento(n, vetor));

    return 0;
}