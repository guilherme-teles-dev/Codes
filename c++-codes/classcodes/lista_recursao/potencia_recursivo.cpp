/*
Descrição: Código para realizar a operação de potênciação
Entrada: Irá receber dois números inteiros, um sendo a base e outro o expoente
Saída: Um número inteiro resultado de uma operação de potênciação.
*/
//Declaração das bibliotecas que serão usadas ao longo da biblioteca;
#include <stdio.h>
//Declaração da função responsável por realizar a potênciação de maneira recursiva.
int potencia(int x, int n){
    //Abertura de condicional de controle de recursividade
    if(n == 1){ //Verifica se é a ultima operação da potênciação
        return x; //Returna o valor sem modifica-lo pois já foi completamente potênciado;
    }
    //Caso ainda existir operações de potênciação restantes, realize chame a função novamente para fazer a multiplicação
    else{
        //A cada chamada recursiva será feito uma multiplicação até que todas as multiplicações da potênciação sejam realizadas.
        return x*potencia(x, n-1);
    }
}
//Declaração do código principal
int main(){
    //Declaração das variáveis responsáveis por guardar a base e o expoente.
    int x, n;
    //Entrada do programa
    scanf("%d %d", &x, &n);
    //Saída do valor potênciado;
    printf("%d elevado a %d é %d.\n", x, n, potencia(x, n));

    return 0;
}