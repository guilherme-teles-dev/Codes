//Declaração das bibliotecas necessárias;
#include <stdio.h> 
//Definição de um tamanho para os vetores;
#define MAX 100
//Declaração da função principal;
int main(void)
{
    //Declaração das variáveis que serão usadas ao longo do programa, incluindo o vetor;
    int n, i, C[MAX], x;
    //Entrada da quantidade de termos que irão ser colocadas dentro do vetor;
    scanf("%d", &n);
    //População do vetor;
    for (i = 0; i < n; i++)
        scanf("%d", &C[i]);
    
    //Entrada do termo que queremos procurando dentro do vetor;
    scanf("%d", &x);
    //Procura do termo dentro do vetor;
    for (i = 0; i < n && C[i] != x; i++); //A condicional de parada é ou chegar ao final do vetor, ou encontrar o termo; 
    //Condicional para verificar se o valor foi encontrado;
    if (i < n) 
        //Se ele foi encontrado, diga a posição em que foi encontrado;
        printf("%d está na posição %d de C\n", x, i);
    //Caso ele não for encontrado, diga que não foi encontrado;
    else
    printf("%d não pertence ao conjunto C\n", x);
    return 0;
}