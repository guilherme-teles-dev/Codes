#include <stdio.h>
int euclides(int a, int b){

    if(a%b==0){
        return b;
    }
    else{
        return euclides(b, a%b);
    }
}
int main(){

    int a, b;
    scanf("%d %d", &a, &b);
    printf("O máximo dividor comum entre %d e %d é: %d.\n", a, b, euclides(a, b));


    return 0;
}