/*
Descrição: Código para escrever os n primeiros termos da sequência fibonacci;
Entrada: Um valor n qualquer que representa a quantidade de termos da sequência fibonacci que queremos exibir;
Saída: Os n termos da sequência escritos;
*/
//Declaração das bibliotecas que irão ser usadas ao longo do código;
#include <stdio.h>
//Declaração da função recursiva que irá escrever os n termos na tela;
void fibonacci(int n, int a, int b){
    //Abertura de condicional para controle de recursão;
    if(n == 0){ //Verifica se todos os termos desejados já foram escritos;
        printf("%d\n", a); //Escreve o último termo desejado da sequência fibonacci;
    }
    else{ //Enquanto ainda precisar escrever os termos da sequência fibonacci:
        printf("%d\n", a); //Escreva o termo
        fibonacci(n-1, b, a+b); //Chame a função novamente porém com o valor contado e o fibonacci somado.
    }
}
//Declaração do código principal;
int main(){
    //Declaração do variável que será responsável por guardar até que posição nós queremos saber da sequência fibonacci.
    int n;
    //Input do programa
    scanf("%d", &n);
    //Chamada da função responsável exibir os termos.
    fibonacci(n, 0, 1);

    return 0;
}