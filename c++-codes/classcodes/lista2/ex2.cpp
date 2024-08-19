#include <stdio.h>
int main(){

    float n1, n2, n3;
    int peso1, peso2, peso3;

    printf("Digite a nota 1:\n");
    scanf("%f", &n1);
    printf("Digite o peso da nota:\n");
    scanf("%d", &peso1);

    printf("Digite a nota 2:\n");
    scanf("%f", &n2);
    printf("Digite o peso da nota:\n");
    scanf("%d", &peso2);

    printf("Digite a nota 3:\n");
    scanf("%f", &n3);
    printf("Digite o peso da nota:\n");
    scanf("%d", &peso3);

    printf("A média final é: %f\n", ((n1*peso1+n2*peso2+n3*peso3)/(peso1+peso2+peso3)));

    return 0;
}