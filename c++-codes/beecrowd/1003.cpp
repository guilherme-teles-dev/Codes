/*
Autor: Guilherme B. Teles
Descrição: Programa que somará dois números
Entrada: Um número a e um número b.
Saída: A soma de a com b
*/
#include <iostream> //Inclui a biblioteca iostream para conseguir realizar a entrada e saída através dos comandos cin e cout.
using namespace std; //Defini o uso dos comandos da biblioteca como std para facilitar a escrita e leitura do código.

//Criação da função de soma de variáveis
int soma(int a, int b){ //Criei uma função chamada soma que recebe variáveis a e b inteiras e retorna uma variável inteira.
    int x = a+b; //Ao mesmo tempo que declarei a variável inteira x, também atribui à ela a soma de a e b.
    return x; //Retornei como saída da função a variáveis recem criada x.
}

//Esse aqui é o código principal
int main(){
    int A, B, X; //Declaro variáveis A, B e X inteiras.
    cin >> A >> B; //Recebo valores do teclado para A e B.
    X = soma(A, B); //Informo A e B como parâmetros para a função soma que criei e atribuo a saída dela a X.
    cout << "SOMA = " << X << endl; //Envio para a minha output a string "SOMA = " seguida do conteúdo de X e uma linha pulada.
}
