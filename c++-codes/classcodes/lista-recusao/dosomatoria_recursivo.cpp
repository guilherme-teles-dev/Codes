/*
Descrição: Função para efetuar a somatória das n primeiras 1/n frações;
Entrada: Um valor inteiro n qualquer;
Saída: Uma soma de frações de formula 1/n com n variando de 1 à n;
*/
//Inclusão das bibliotecas que serão usadas;
#include <stdio.h>
//Declaração da função recursiva que irá realizar a somatória;
double do_somatoria(int n){ //Função recebe uma variável n referente ao range de soma;
    //Essa função atua fazendo a soma recursiva da menor fração até a maior, que é a primeira, no caso 1/1;

    //Condicional para decidir qual fração deve ser retornada;
    if(n == 1){ //Em caso de ser o último termo a ser somado, retorna 1;
        return  n; //Retorna o maior valor;
    }
    else{ //Caso ainda ter somas para ser feitas, monta uma fração e soma ela com a próxima fração maior;
        double frac = 1.0/n; //Montagem da fração;
        return frac + do_somatoria(n-1); //Retorno da fração somada à proxima maior;
    }
}
//Código principal;
int main(){
    //Declaração da variável n que irá ser usada para armazenar o range de soma;
    int n;
    //Input de valor para n;
    scanf("%d", &n);
    //Output de somatória do código;
    printf("A soma das frações é igual à: %lf\n", do_somatoria(n));

    return 0;
}