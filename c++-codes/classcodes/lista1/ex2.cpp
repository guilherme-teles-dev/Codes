#include <stdio.h>
int main(){
    int n;
    int cont= 0, cont_p = 0, soma_p = 0;
    scanf("%d", &n);
    while(n != 0){
        int digito = n%10;
        if (digito%2==0){
            cont_p ++;
            soma_p = soma_p+digito;
        }
        cont++;
        n = n/10; //Sempre será inteiro visto que ambos
    }
    printf("%d digitos foram informados.\n", cont);
    
    if(cont_p!=0){
        printf("Média dos dígitos pares existentes: %.2f\n", float(soma_p)/cont_p);
    }
    else{
        printf("Não existem dígitos pares no número informado.\n");
    }
    return 0;
}