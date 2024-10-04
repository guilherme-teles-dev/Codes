/*
Descrição: Código para realizar fatoração recursivamente
Entrada: Um valor inteiro qualquer
Saída: O fatorial dele.
*/

#include <stdio.h>
int fat(int num, int position){
    if(position == 1){
        return num;
    }
    else{
        position = position-1;
        return fat(num*position, position);
    }
}
int main(){
    int num;
    scanf("%d", &num);
    num = fat(num, num);
    printf("O fatorial é %d\n", num);
    return 0;
}