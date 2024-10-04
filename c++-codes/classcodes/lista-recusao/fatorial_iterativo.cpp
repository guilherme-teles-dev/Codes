#include <stdio.h>
int main(){
    int num, fat;
    scanf("%d", &num);
    fat = num;
    for(int i = 1; i < num; i++){
        fat = fat*i;
    }
    printf("O fatorial de %d é: %d\n", num, fat);

    return 0;
}