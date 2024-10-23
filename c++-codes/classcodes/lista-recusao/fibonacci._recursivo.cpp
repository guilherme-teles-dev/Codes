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
        printf("%d\n", a);
    }
    else{
        printf("%d\n", a);
        fibonacci(n-1, b, a+b);
    }
}

int main(){
    int n;
    scanf("%d", &n);
    
    fibonacci(n, 0, 1);

    return 0;
}