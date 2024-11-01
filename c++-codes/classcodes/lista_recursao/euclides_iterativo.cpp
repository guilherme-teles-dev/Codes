/*
Descrição: Código para encontrar o máximo divisor comum entre dois números utilizando o algoritmo de Euclides;
Entrada: Dois números inteiros "a" e "b";
Saída: O máximo dividor comum entre "a" e "b";
*/
//Declaração das bibliotecas que serão necessárias para o código.
#include <stdio.h>
//Declaração da função iterativa para realizar o algoritmo de euclides.
int euclides(int a, int b){
    //Looping para decompor "b" até ele virar um múltiplo de "a", no caso, vamos decompor "b" até ele virar o mdc;
    while(a%b != 0){
        //Declara uma variável auxiliar para auxiliar na troca de valores entre variáveis;
        int c = 0;
        //Realiza a operação de euclides;
        c = a%b;
        a = b;
        b = c;
    }
    return b;
}
//Declara o código principal
int main(){
    //Declara as variáveis que serão responsáveis por armazenar os valores que serão encontradas as variávies euclidianas;
    int a, b;
    //Input das váriaveis "a" e "b" do teclado;
    scanf("%d %d", &a, &b);
    //Output do programa;
    printf("O máximo divisor comum entre %d e %d é %d.\n", a, b, euclides(a, b));

    return 0;
}