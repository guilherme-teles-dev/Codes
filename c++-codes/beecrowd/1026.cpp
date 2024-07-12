/*
Autor: Guilherme B. Teles
Descrição: Código para realizar soma de de números decimáis, porém em binário e com bitwise sempre 0.
Entrada: Dois números inteiros equivalentes até 32 bits.
Saída: O resultado da soma dos dois números, porém convertido de binário e sem bitwise.
*/
#include <stdio.h> //Inclui nesse código os comandos básicos do C

//Código principal
int main(){
    unsigned int n, m; //Declara duas variáveis n e m como inteiras e sem sinais, declarar uma variável sem sinal quer dizer que ela pode alcançar numeros positivos mais altos.
    
    //Abertura de looping
    while(scanf("%u %u", &n, &m) != EOF){ //Recebe dois numeros e os guarda em m e n até não conseguir mais fazer isso.
                    printf("%u\n", n ^ m); //Aqui é impresso o resultado de uma comparação bitwise bit a bit
    }
    return 0; //Informa para o terminal que o programa conseguiu chegar no final sem problemas de execução.
}