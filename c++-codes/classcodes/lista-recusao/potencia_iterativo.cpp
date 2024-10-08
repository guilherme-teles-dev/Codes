#include <stdio.h>
int potencia(int x, int n){
    int potencia = x;
    for(int i = 1; i < n; i++){
        potencia = potencia*x;
    }
    return potencia;

}
int main(){

    int x, n;
    scanf("%d %d", &x, &n);

    printf("O resultado de %d elevado a %d é %d.\n", x, n, potencia(x, n));

    return 0;
}