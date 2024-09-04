
#include <stdio.h>
#define N 10
int main(void){
    int V[N], *p;

    printf("Informe %d números: ", N);
    for(p = V; p < V + N; p++)
        scanf("%d", p);
    printf("Em ordem inversa: ");
    for (p = V + N - 1; p >= V; p--)
        printf("%d ", *p);
    printf("\n");

    return 0;
}