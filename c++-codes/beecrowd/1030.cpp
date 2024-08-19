/*
Autor: Guilherme B. Teles
Descrição: Algorítmo para dizer qual será o ultimo homem morto em um suicídio coletívo em roda.
Entrada: O número de casos e em seguida cada caso contendo o número de pessoas e o primeiro a ser morto.
Saída: Quem foi o único que não morreu
*/
#include <iostream>
using namespace std;
int main(){
    int casos; //Crio uma variável que vai guardar quantos casos precisam ser executados.
    cin >> casos; //Recebo a quantidade de dados.
    
    //Inicio um looping.
    for(int caso = 0; caso < casos; caso++){ //Vai executar pelo número de casos informados.
        //Criação de variáveis
        int pessoas, inicio; //Declaro variáveis que irão receber informações sobre o problema, sendo pessoas o número de pessoas na roda e início a primeira pessoa a ser morta.
        int mortos = 0;
        int proximo = inicio;

        cin >> pessoas >> inicio; //Recebo as informações.
        int roda[pessoas] = {1}; //Crio um array vazio com todas as pessoas vivas.
        
        //Inicio de um loopings
        while(mortos < pessoas-1){ //Crio um looping que vai matar as pessoas e só vai parar quando sobrar um.
            
            if(proximo < pessoas){ //Condicional para simular efeito de circulo.
                proximo = proximo-pessoas;
            }
            roda[proximo]
        }
    }
    return 0;
}