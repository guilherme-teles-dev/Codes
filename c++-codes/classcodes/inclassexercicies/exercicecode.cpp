/*
Descrição: Algoritmo para cadastrar carros
*/
//Declaração de bibliotecas que irão ser usadas
#include <stdio.h> //Biblioteca de comandos básicos.
#include <string.h> //Biblioteca de manipulação de strings

#define tamanho_vetor 30 //Definição de tamanho de vetor

//Criação de registro de carros
struct carro{
    char marca[15];
    int ano;
    float preco;
};

//Função para cadastrar carros
carro cadastrar_carro(){
    char marca[15];
    int ano;
    float preco;

    printf("Digite a marca do carro: ");
    scanf(" %[^\n]", marca); //Aparentemente isso foi feito para evitar problema de buffer
    //scanf("%s", marca);

    printf("Digite o ano do carro: ");
    scanf("%d", &ano);

    printf("Digite o preço do carro: ");
    scanf("%f", &preco);

    carro carro_atual;
    strcpy(carro_atual.marca, marca);
    carro_atual.ano = ano;
    carro_atual.preco = preco;

    return carro_atual;
}

//Função para listar carros
void listas_carros(carro carros[], int carros_cadastrados){
   // printf("Entrou na função");
    for(int c = 0; c < carros_cadastrados; c++){
        printf("\nMarca: %s\n", carros[c].marca);
        printf("Ano: %d\n", carros[c].ano);
        printf("Preço: %f\n", carros[c].preco);
    }
   // printf("Saiu da função");
}

//Função para tirar a média dos carros cadastrados
void media_precos(carro carros[], int carros_cadastrados){
    float preco_total = 0;
    for (int i = 0; i < carros_cadastrados; i++)
    {
        preco_total = preco_total + carros[i].preco;
        //preco_total = preco_total + carros[i].preco/carros_cadastrados;
    }

    // O ENUNCIADO PEDE A MÉDIA DOS PREÇOS DOS CARROS DE UM ANO ESPECÍFICO. VC NÃO ESTÁ FAZENDO ISSO
    // MAS SIM, FAZENDO A MÉDIA DE TODOS OS CARROS

    preco_total = preco_total/carros_cadastrados; // essa linha não tinha. De fato vc tem que ver se carros_cadastrados != 0 antes de fazer esta divisão //Basicamente pode dar problema se eu tentar tirar a média sem ter carro cadastrado.

    printf("A média de preços é: %.2f\n", preco_total);

}

//Código principal
int main(){
    //Declaração de variáveis que irão ser usadas
    int carros_cadastrados = 0;
    carro carros[tamanho_vetor];  // EU QUE COLOQUEI AQUI
    char opcao; // EU QUE COLOQUEI AQUI

    //Criação de looping principal do programa
    while (1)
    {
        //printf("carros_cadastrados no início do looping: %d\n", carros_cadastrados);
        //char opcao; // PQ DECLARAR TODA VEZ A "MESMA" VARIÁVEL? //Aparentemente declarar sempre a mesma variável pode dar problema de memória.
       
        printf("\n---Funções---\n");
        printf("[C] - Cadastrar\n[L] - Listar Carros;\n[T] - Tirar a média;\n[F] - Finalizar;\nDigite qual função deseja executar[C/L/T/F]:\n");
        scanf(" %c", &opcao); // É PRECISO COLOCAR O -ESPAÇO- ANTES DO %c //Aparentemente de faltar o espaço antes do C pode haver um problema de buffer.

        //carro carros[tamanho_vetor]; // NÃO PODE SER AQUI, SENÃO VC ESTARIA TODA VEZ DECLARANDO UM NOVO VETOR! //Mesmo problema anterior, buffer
        if(opcao == 'C'){
                carros[carros_cadastrados] = cadastrar_carro();
                //printf("%s\n", carros[carros_cadastrados].marca);
                //printf("%d\n", carros[carros_cadastrados].ano);
                //printf("%.2f\n", carros[carros_cadastrados].preco);
                carros_cadastrados++;
        }
        else if(opcao=='L'){
            if(carros_cadastrados == 0){
                printf("Nenhum carro cadastrado\n");
            }
            else{
                listas_carros(carros, carros_cadastrados);
            }

        }
        else if(opcao=='T'){

            media_precos(carros, carros_cadastrados);
        }
        else if(opcao=='F'){break;}
       // printf("carros_cadastrados no final do looping: %d\n", carros_cadastrados);
    }
    return 0;
}
