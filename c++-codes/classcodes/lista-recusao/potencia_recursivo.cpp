#include <stdio.h>
int potencia(int x, int n){
    if(n == 1){
        return x;
    }
    else{
        return x*potencia(x, n-1);
    }
}
int main(){

    int x, n;
    scanf("%d %d", &x, &n);

    printf("%d elevado a %d é %d.\n", x, n, potencia(x, n));

    return 0;
}