#include <stdio.h>
int euclides(int a, int b){
    while(a%b != 0){
        int c = 0;
        c = a%b;
        a = b;
        b = c;
    }
    return b;
}
int main(){

    int a, b;
    scanf("%d %d", &a, &b);
    printf("O máximo divisor comum entre %d e %d é %d.\n", a, b, euclides(a, b));

    return 0;
}