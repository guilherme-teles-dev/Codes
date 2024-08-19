#include <stdio.h>

int main(){

    float salario, porcentagem;

    scanf("%f%f", &salario,&porcentagem);

    printf("%.2f\n", salario*(1+porcentagem/100));

    return 0;
}