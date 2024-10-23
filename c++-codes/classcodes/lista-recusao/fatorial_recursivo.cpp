/*
Descrição: Código para realizar fatoração recursivamente
Entrada: Um valor inteiro qualquer
Saída: O fatorial dele.
*/
//Declaração das bibliotecas que deverão ser usadas ao longo do programa;
#include <stdio.h>
//Declaração que irá realizar o fatorial do programa;
int fat(int num, int position){
    //Abertura de condicional de controle de recursão;
    if(position == 1){ //Verifica se position, que é o contador de multiplicações, já se tornou 1, ou seja, já realizou todas as multiplicações necessárias;
        return num;
    }
    else{ //Caso position não for 1, multiplica o número pela multiplicação atual e reduz 1 de position;
        position = position-1;
        return fat(num*position, position); //A ideia central dessa recursão é que na medida que position se aproxima de 1, ele multiplique o número que precisa ser fatorado;
    }
    //Era necessário que position fosse um valor externo a função pois ele se perderia se fosse declarado dentro da função;
}
//Declaração do código principal;
int main(){
    //Declara a variável que irá receber o valor que sofrerá o fatorial;
    int num;
    //Entrada do programa;
    scanf("%d", &num);
    //Chamada da função (Reaproveitando a variável porque eu não sou porco);
    num = fat(num, num);
    //Saída do programa;
    printf("O fatorial é %d\n", num);
    return 0;
}