/*
Autor: Guilherme B. Teles
Descrição: Programa para calcular a área de um circulo.
Entrada: O ráio do circulo.
Saída: A área do circulo.
*/
//Inclusão de bibliotecas
#include <iostream> //Inclusão da biblioteca iostream para realizar entrada e saída de dados através de cin e cout
#include <iomanip> //Incluo a biblioteca iomanip para formatar minha saída.

using namespace std; //Faço uso da função namespace std para aumentar a legibilidade do meu código ao mesmo tempo que facilito a programação.

//Crio uma função para calcular a área do circulo através do raio
double r(double a){ //Informo que minha função vai receber apenas um paramêtro a do tipo double e que retornará um variável r do tipo double também
    const double pi = 3.14159; //Declaro uma variável constante, ou seja, imutável, do tipo double, chamada pi e atribúo a ela o valor de pi.
    double result = pi * (a*a); //Faço a portabilidade da formula da área e uso ela para realizar o calculo e posteriormente atribuo ela à variável do tipo double recem iniciada chamada result;
    return result; //Retorno a variável result para fora da função.
}

//Inicio o código principal;
int main(){
    cout << fixed << setprecision (4); //Aqui estou setando alguns parametros de formatação para minha saída para conter apenas 4 casas decimais, isso usando a biblioteca iomanip.

    double area, raio; //Aqui declarei as variáveis area e raio como variáveis do tipos double.

    cin >> raio; //Recebi um valor em raio.

    area = r(raio); //Coloquei o valor recebido em raio dentro da função que eu criei para calcular a area e pus o resultado retornado dessa função dentro da variáveis area.
    cout << "A=" << area << endl; //Tendo a área em mãos, eu outputei a string "A=", depois o conteúdo da variáveis area e posteriormente uma linha pulada.

    return 0; //Retornei para meu terminal o valor zero para indicar que meu código conseguiu chegar no final sem maiores problemas.
}