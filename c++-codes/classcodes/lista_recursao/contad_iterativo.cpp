/*
Descrição: Código para contar quantos algarismos compõem o número digitado n;
Entrada: Um número inteiro n.
Saída: Um número inteiro referente a quantidade de algarismos que compoem o número inteiro n.
*/

//Declaração de bibliotecas que serão usadas ao longo do programa.
#include <stdio.h>
//Declaração da função iterativa que irá contar quando números compõem determinado número n;
int conta_numeros(int n){
    //Declaração de variável que irá servir de contador;
    int contador = 0;
    //Inicialização de condicional onde o if irá verificar se o número n possui apenas um algarismo, essa verificação é necessária para proteger a lógica do else;
    if(n < 10){
        return 1; //Em caso do número n ser menor que 10, ele terá apenas um algarismo, portanto não é necessário realizar soma nenhum e podemos retornar apenas 1;
    }
    else{ //Em caso dele ser maior que 10 podemos realizar uma soma tranquilamente sem maiores conflitos de lógica;
        contador++; //Soma-se 1 no contador pois já temos certeza que ele tem pelo menos a casa das unidades;
        //Inicialização de looping para contar quantas casas o número tem contando quantas vezes podemos dividir ele por 10;
        while(n >= 10){
            n = n/10;
            contador++;
        }
    }
    //Retorna a quantidade de vezes que o número é dividido por 10, vezes essas que são equivalentes a quantidade de algarismos que compõem o número;
    return contador;
}
//Declação do código principal;
int main(){
    //Declaração da variável que irá receber o número que devemos contar os algarismos;
    int n;
    //input de n;
    scanf("%d", &n);
    //Output da soma dos algarismos de n;
    printf("No número %d, existem %d numeros.\n", n, conta_numeros(n));

    return 0;
}