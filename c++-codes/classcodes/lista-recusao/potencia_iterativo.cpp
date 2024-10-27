/*
Descrição: Código para realizar a operação de potênciação;
Entrada do programa: Um valor inteiro de base e um valor inteiro de potência;
Saída do programa: O resultado da potênciação da base pela potência;
*/
//Declaração das bibliotecas que serão usadas ao longo do código
#include <stdio.h>
//Declaração da função que irá realizar a potênciação recursivamente;
int potencia(int x, int n){
    //Declaração da variável que irá ser potênciada;
    int potencia = x;
    //Abertura de looping para realizar a potênciação
    for(int i = 1; i < n; i++){
        potencia = potencia*x;
    }
    return potencia;

}
//Declaração do código principal
int main(){
    //Declaração das variáveis que irão ser usadas no programa.
    int x, n;
    //Entrada do programa
    scanf("%d %d", &x, &n);
    //Saída do programa
    printf("O resultado de %d elevado a %d é %d.\n", x, n, potencia(x, n));

    return 0;
}