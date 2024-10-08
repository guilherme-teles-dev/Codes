/*
Descrição: Código para somar os digitos de um inteiro n digitado.
Entrada: Um número inteiro n.
Saída: A soma dos digitos que compoem o númeor n.
*/
#include <stdio.h>
int soma_digitos(int n){

    int quociente, resto;
    if(n < 10){
        return n;
    }
    else{
        quociente = n/10;
        resto = n%10;
        return resto+soma_digitos(quociente);
    }

}
int main(){

    int n;
    scanf("%d", &n);
    printf("A soma dos digitos do número %d é %d.\n", n, soma_digitos(n));

    return 0;
}