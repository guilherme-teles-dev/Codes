/*
Descrição: Código para verificar se existe algum número par dentro de um vetor
Entrada: A quantidade de números que serão digitadas e os próprios números
Saída: Se existe ou não algum par dentro do vetor;
*/
//Declaração das bibliotecas que serão usadas;
#include <stdio.h> //Biblioteca de comandos padrões
#include <stdlib.h> //Biblioteca de controle de memória
//Declaração da função recursiva que confere se existem números pares dentro da função
bool tem_par(int *vetor, int tamanho_vetor){
    //Comando que me ajudou no debug, deixei para a senhora ver melhor como foi feito;
    printf("Número verificado: %d\n", *vetor);
    //Abertura de condicional de controle de recursão e proteção de lógica do código
    if(tamanho_vetor < 1 && *vetor%2==1){  //Aqui é verificado se chegamos ao final do vetor sem achar um par;
        return false;
    }
    else if(*vetor%2==0){ //Aqui verificamos se achamos um par;
        return true;
    }
    else{ //Aqui percorremos o vetor
        return tem_par(vetor+1, tamanho_vetor-1);
    }
}
//Declaração do código principal
int main(){
    //Declaração das variáveis que irão guardar o tamanho do vetor e o endereço dele respectivamente
    int tamanho_vetor, *vetor;
    //Entrada do tamanho do vetor, ou seja, a quantidade de números que serão digitados;
    scanf("%d", &tamanho_vetor);
    //Alocação dinâmica do vetor
    vetor = (int *) malloc(tamanho_vetor*sizeof(int));
    //População do vetor
    for(int i = 0; i < tamanho_vetor; i++){
        scanf("%d", &vetor[i]);
    }
    //Declaração de variável que irá guardar se existem ou não númeoros pares dentro do vetor
    bool resultado;
    //Chamada da função para procurar números pares dentro da função e atribuição de valor booleano à variável resultado, se true,
    //existe par, se false, não existe par;
    resultado = tem_par(vetor, tamanho_vetor);
    //Condicional para saída do programa que irá dizer se existe ou não par no vetor;
    if(resultado == true){
        printf("O vetor tem par.\n");
    }
    else{
        printf("O vetor não tem par.\n");
    }
    //Liberação de memória alocada;
    free(vetor);
    return 0;
}