/*
Descrição:
Programa para calcular salário do funcionário.

Input:
Número da matrícula do funcionário, horas trabalhadas, valor da hora, número de filhos.

Output:
Salário + 10% de acrescimo por filho.
*/

#include <stdio.h> // Import de biblioteca 

int main(){

    int n_matricula, horas_trabalhadas, numero_filhos;
    float valor_h;

    printf("Digite o número de matrícula do funcionário: \n");
    scanf("%d", &n_matricula);
    printf("Digite o número de horas trabalhadas mensais: \n");
    scanf("%d", &horas_trabalhadas);
    printf("Digite a quantidade de filhos: \n");
    scanf("%d", &numero_filhos);
    printf("Digite o valor da hora trabalhada: \n");
    scanf("%f", &valor_h);
    printf("O salário desse funcionário será: R$%.2f\n", valor_h*horas_trabalhadas*(1+(numero_filhos/10.0)));

    return 0;
}