/*
Descrição: Código para contar a quantidade de algarismos que compoem o número digitado n.
Entrada: Um número inteiro n;
Saída: Um número inteiro referente a quantidade de algarismos presente dentro do número n.
*/
//Import de bibliotecas que serão utilizadas ao longo do programa
#include <stdio.h>
//Declaração da função recursiva que irá contar quantos algarismos existem dentro do número.
int contador(int n){
    //Abertura de condicional que irá dividir o número por 10 até restar apenas um algarismo.
    if(n < 10){ //Verifica se o número é número é menor do que 10, ou seja, possúi apenas um algarismo.
        return 1;
    }
    else{ //Em caso do número ainda ser maior que 10, divida ele por 10 e chame a função novamente.
        n = n/10;
        return 1 + contador(n);
    }
}
//Declaração do código principal
int main(){
    //Declaração da variável que irá receber o valor inteiro n que devera ter os algarismos contados
    int n;
    scanf("%d", &n);
    //Output da quantidade de algarismos do numero n.
    printf("A quantidade de digitos presentes dentro do número %d é %d.\n", n, contador(n));

    return 0;
}