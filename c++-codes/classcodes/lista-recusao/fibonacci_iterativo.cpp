/*
Descrição: Código para escrever os n primeiros termos da sequência fibonacci
Entrada: Um valor inteiro n qualquer
Saída: A sequância fibonacci até aquele valor
*/
//Declaração da biblioteca que será usada ao longo do programa;
#include <stdio.h>
//Declaração da função iterativa void que irá mostrar os termos da sequência fibonnaci; 
void fibonacci(int n_esimo_termo){
    //Declaração dos valores iniciais da sequência fibonnaci;
    int a1= 0, a2=1;
    //Abertura de condicional para proteção de lógica de código;
    if(n_esimo_termo == 0){ //Verifica se o enesimo termo não é 0;
        printf("0 não é um valor válido.\n");
    }
    else{
        printf("%d\n", a1); //Se ele é maior que 0, no mínimo ele é um, logo é possível imprimir o 1 e continuar o código;
        for(int i=0; i<n_esimo_termo-1; i++){ //Escreve os termos até o enesimo, nota que eu subtrai 1 do enesimo pois já escrevemos na linha anterior;
            //Apartir daqui o código irá girar em torno do segundo termo, ele irá receber o resultado de todas as operações aritméticas;
            printf("%d\n", a2);
            //Declara variável auxiliar para auxiliar na troca de valores entra veriáveis;
            int aux;
            //Realiza troca das variáveis passando o a2 para o a1
            aux = a1;
            a1 = a2;
            //Atribui a a2 a soma dos termos a1 e o antigo a2;
            a2 = aux+a1;
        }
    }
}
//Declaração do código principal;
int main(){
    //Declaração da variável que irá armazenar a profundidade na sequência fibonnaci que nós queremos;
    int n_esimo_termo;
    //Entrada do programa;
    scanf("%d", &n_esimo_termo);
    //Chamada da função que irá realizar a sequência;
    fibonacci(n_esimo_termo); //Nesse código eu optei por realizar a output do código embarcada na função pois seria mais fácil, visto que a output faz parte da lógica do programa;

    return 0;
}