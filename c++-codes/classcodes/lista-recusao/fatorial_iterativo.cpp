/*
Descrição: Código que irá realizar o vatorial de um número "num";
Entrada: Um numero inteiro "num" qualquer;
Saída: O fatorial desse número "num";
*/
//Declaração da biblioteca que irá ser usada ao longo do programa;
#include <stdio.h>
//Declaração da função principal
int main(){
    //Declaração das variáveis que irão ser usadas ao longo do programa, sendo "num" a variável que irá receber o número que deve sofrer o fatorial e fat o valor que irá ser sofrer o fatorial de fato;
    int num, fat;
    //Entra do programa;
    scanf("%d", &num);
    //Atribuimos o valor de num ao fat pois iremos usar o num apenas como referência e iremos realizar o fatorial no fat;
    fat = num;
    //Abertura de looping para realizar o fatorial;
    for(int i = 1; i < num; i++){ //Perceba que esse looping irá funcionar num vezes, ou seja, o num está sendo usada de referência de execução, enquanto quem irá ser sofrer o fatorial de fato é o fat;
        fat = fat*i; //Caso tivessemos usado o num aqui, o looping funcionaria para sempre e o fatorial não ia dar certo, por isso, apesar de ter o mesmo valor, o fat e o num tem funções diferentes;
    }
    //Output do programa;
    printf("O fatorial de %d é: %d\n", num, fat);

    return 0;
}