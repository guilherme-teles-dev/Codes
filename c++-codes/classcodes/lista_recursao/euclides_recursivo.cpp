/*
Descrição: Código para encontrar o MDC entre um inteiro "a" e outro "b" fazendo uso do algorítmo de euclides;
Entrada: Dois valores inteiros "a" e "b";
Saída: O MDC deles;
*/
//Declaração das bibliotecas que serão usadas ao longo do programa;
#include <stdio.h>
//Declaração da função recursiva que irá realizar a operação de euclides;
int euclides(int a, int b){
    //Abertura de condicional responsável por regular a recursão;
    if(a%b==0){ //Caso "b" seja multiplo de "a", retorne b;
        return b;
    }
    else{//Se não chame a função novamente porém para "b" e "o resto da divisão inteira entre a e b";
        return euclides(b, a%b); //Com isso, enquanto a função não achar o múltiplo, ela dividirá o número sucessivamente até achar-lo;
    }
}
//Declaração do código principal
int main(){
    //Declaração das variáveis que irão guardar os valores que irá ser tirado o MDC;
    int a, b;
    //Input dos valores "a" e "b";
    scanf("%d %d", &a, &b);
    //Output do programa;
    printf("O máximo dividor comum entre %d e %d é: %d.\n", a, b, euclides(a, b));


    return 0;
}