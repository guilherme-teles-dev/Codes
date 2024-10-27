/*
Descrição: Código para somar os digitos de um inteiro n digitado.
Entrada: Um número inteiro n.
Saída: A soma dos digitos que compoem o númeor n.
*/
//Declaração das bibliotecas que serão usadas ao longo do programa;
#include <stdio.h>
//Declaração da função recursiva que irá contar os digitos do número recursivamente;
int soma_digitos(int n){
    //Declaração das variáveis que irão quebrar o número
    int quociente, resto;
    //Declaração da condicional de controle de recursividade
    if(n < 10){ //Verifica se resta apenas um digito para se somado
        return n; //Se sim, soma apenas mais o digito atual
    }
    //No caso padrão nós dividimos o número e operamos o quociente dele;
    else{
        quociente = n/10;
        resto = n%10;
        return resto+soma_digitos(quociente);
    }

}
//Declaração do código principal;
int main(){
    //Declaração da função que irá receber o número
    int n;
    //Entrada do programa
    scanf("%d", &n);
    //Saída do programa
    printf("A soma dos digitos do número %d é %d.\n", n, soma_digitos(n));

    return 0;
}