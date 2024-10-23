/*
Descrição:
Entrada:
Saída:
*/
#include <stdio.h>
#include <stdlib.h>
bool tem_par(int *vetor, int tamanho_vetor){
    printf("Número verificado: %d\n", *vetor);
    if(tamanho_vetor < 1 && *vetor%2==1){
        return false;
    }
    else if(*vetor%2==0){
        return true;
    }
    else{
        return tem_par(vetor+1, tamanho_vetor-1);
    }
}
int main(){
    int tamanho_vetor, *vetor;
    scanf("%d", &tamanho_vetor);
    
    vetor = (int *) malloc(tamanho_vetor*sizeof(int));
    for(int i = 0; i < tamanho_vetor; i++){
        scanf("%d", &vetor[i]);
    }

    bool resultado;
    resultado = tem_par(vetor, tamanho_vetor);

    if(resultado == true){
        printf("O vetor tem par.\n");
    }
    else{
        printf("O vetor não tem par.\n");
    }
    free(vetor);
    return 0;
}