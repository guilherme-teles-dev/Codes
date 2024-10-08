/*
Descrição: Código para somar todos os digitos de um inteiro n digitado.
Entrada: Um número inteiro n.
Saída: A soma dos digitos que compoem n.
*/
#include <stdio.h>
int soma_digitos(int n){
    if(n < 10){
        return n;
    }
    else{
        int soma=1;
        while(n >= 10){
            soma = soma + n%10;
            n = n/10;
        }
        return soma;
    }
}
int main(){

    int n;
    scanf("%d", &n);
    printf("A soma dos digitos que compoem o número %d é %d.\n", n, soma_digitos(n));

    return 0;
}