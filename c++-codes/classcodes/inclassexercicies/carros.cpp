#include <stdio.h>
#include <string.h>

#define tamanho_vetor 30

struct carro{
    char marca[15];
    int ano;
    float preco;
};

carro cadastrar_carro(){
    char marca[15];
    int ano;
    float preco;

    printf("Digite a marca do carro: ");
    scanf("%s", marca);

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

void listas_carros(carro carros[], int carros_cadastrados){
    printf("Entrou na função");
    for(int c = 0; c < carros_cadastrados; c++){
        printf("Marca: %s\n", carros[c].marca);
        printf("Ano: %d\n", carros[c].ano);
        printf("Preço: %f\n", carros[c].preco);
    }
    printf("Saiu da função");
}

void media_precos(struct carro carros[], int carros_cadastrados){
    float preco_total = 0;
    for (int i = 0; i < carros_cadastrados; i++)
    {
        preco_total = preco_total + carros[i].preco/carros_cadastrados;
    }

    printf("A média de preços é: %.2f\n", preco_total);

}

int main(){
    int carros_cadastrados = 0;
    while (1){
        printf("carros_cadastrados no início do looping: %d\n", carros_cadastrados);
        char opcao;
        printf("\n---Funções---\n");
        printf("Cadastrar[C];\nListar Carros[L];\nTirar a média[T];\nFinalizar[F];\nDigite qual função deseja executar[C/L/T/F]:\n");
        scanf(" %[^\n]", &opcao);
        carro carros[tamanho_vetor];
        if(opcao == 'C'){
                carros[carros_cadastrados] = cadastrar_carro();
                printf("%s\n", carros[carros_cadastrados].marca);
                printf("%d\n", carros[carros_cadastrados].ano);
                printf("%.2f\n", carros[carros_cadastrados].preco);
                carros_cadastrados++;
                printf("carros_cadastrados no final do cadastrado: %d\n", carros_cadastrados);
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
        printf("carros_cadastrados no final do looping: %d\n", carros_cadastrados);
    }
    return 0;
}