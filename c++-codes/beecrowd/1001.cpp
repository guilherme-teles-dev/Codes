/*
Autor: Guilherme B. Teles
Descrição: Código para somar dois números.
Entrada: Dois números A e B.
Saída: Uma soma X resultante da soma de A com B.
*/
#include <iostream> //Incluo a biblioteca iostream para realizar o modelo de input cin e output cout.
using namespace std; //Informo para meu compilador que irei usar a sintaxe simples de input e output.

//Crio uma função para realizar a soma entre dois números.
int soma(int a, int b){ //Essa função recebera dois valores inteiros a e b e terá uma saída inteira.
    int r = a+b; //Declaro uma variável r como inteira e atribuo o valor dela como a soma de a e b.
    return r; //Retorno como saída dessa função a variável r.
}

//Aqui é meu código principal que recebeu o nome de main e onde de fato a mágica acontece.
int main(){
    int A, B, X; //Declarei três variáveis A, B e X como inteiras.
    cin >> A >> B; //Inputei valores do teclado dentro de A e B.
    X = soma(A, B); //Coloquei tanto A quanto B dentro da função soma que criei mais cedo e atribuí o resultado dela em X.
    cout << "X = " << X << endl; //Outputei primeiramente "X = " e depois o valor de X e depois uma linha pulada.
    return 0; //Informei para meu terminal que meu código chegou ao final.
}