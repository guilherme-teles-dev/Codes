/*
Descrição:
Entrada:
Saída:
*/
#include <stdio.h>
#include <stdlib.h>
int busca_binaria(int n, int *v, int valor){
    if(){

    }
    else{
        if(n%2==0){
            if(v[n/2] > valor){
                
            }
            else{}
        }
        else{
            if(){}
            else{}
        }
    }
}
int main(){

    int n, *v;
    scanf("%d", &n);

    v = (int *) malloc(n*sizeof(int));

    for(int i=0; i<n;i++){
        scanf("%d", &v[i]);
    }
    bool continua = true;
    while(continua){
        int valor, posicao;
        scanf("%d", &valor);
        if(valor == -1){
            continua = false;
        }
        else{
            posicao = busca_binaria(n, v, valor);
            printf("O valor está na posição: %d\n", posicao);
        }
    }

    return 0;
}