/*
Descrição: Código para somar todos os digitos de um inteiro n digitado.
Entrada: Um número inteiro n.
Saída: A soma dos digitos que compoem n.
*/
//Declaração das bibliotecas que iremos usar ao longo do programa
#include <stdio.h>
//Declaração da função recursiva que irá contar quantos digitos existem em determinado número
int soma_digitos(int n){
    //Variável de controle de proteção de lógica de código, ela irá garantir que nosso número não possui apenas um digito;
    if(n < 10){
        return n;
    }
    //Caso ela tiver mais de um digitio, ai sim usamos a logica conhecida de sucessivas divisões por 10 para verificar quantos digitos existem.
    //É importante dizer que essa técnica não funcionaria se fosse menos de dois digitos, por isso a necessidade de controle de fluxo;
    else{
        int soma=1;
        //Aqui é onde serão feitas as sucessivas divisões por 10;
        while(n >= 10){
            soma = soma + n%10;
            n = n/10;
        }
        return soma;
    }
}
//Declaração do código principal
int main(){
    //Declaração da variável que irá receber o digito
    int n;
    //Entrada do programa;
    scanf("%d", &n);
    //Saída da quantidade de digitos que existem dentro do número digitado;
    printf("A soma dos digitos que compoem o número %d é %d.\n", n, soma_digitos(n));

    return 0;
}