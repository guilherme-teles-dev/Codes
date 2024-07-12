/*
Autor: Guilherme B. Teles
Descrição: Código para identificar ordem crescente ou decrescente.
Entrada: Dois números.
Saída: Crescente, Decrescente ou Nada.
*/
#include <iostream> //Incluo a biblioteca que vai me permitir realizar entradas e saídas de dados através de cin e cout.
using namespace std; //Utilizo o modo std para facilitar a leitura e escrita dos comandos de bibliotecas.

//Aqui eu começo meu código principal.
int main(){
    bool continua_o_codigo = true; //Crio uma variável para guardar a necessidade de continuar ou não meu código.
    while (continua_o_codigo){ //Crio um looping que executará enquanto meu código necessitar continuar.
    int numero1, numero2; //Declaro duas variáveis do tipo inteiro que irão receber os números do usuário.
    cin >> numero1 >> numero2; //Recebo meus dois números e guardo ambos nas devidas variáveis, é interessante notar que mesmo que os números estejam divididos por espaço, o mecanismo da linguagem define que ao fazer uma input em uma variáveis do tipo inteiro, ele lerá do buffer apenas um inteiro, se orientando assim pelo espaço.
    
    //Criação de uma estrutura condicional para fazer a comparação dos dois números.
    if (numero1 > numero2){ //Verifico se o primeiro número é maior que o segundo.
        cout << "Decrescente" << endl; //Em caso de ser verdadeiro, imprimo Decrescente e uma quebra de linha.
    }
    else if(numero2 > numero1){ //Verifico se o segundo número é maior que primeiro.
        cout << "Crescente" << endl; //Em caso de ser verdadeiro, impremo Crescente e uma quebra de linha.
    }
    else{ //Se todas as verificações anteriores foram falsas, significa que ambos os números são iguais e portanto posso finalizar o programa.
        continua_o_codigo = false; //Informo para minha variáveis de monitoramento que meu programa pode ser encerrado alterando o valor dela para falso e fazendo com que o próximo looping não execute.
    }
    }
    return 0; //Retorno para meu terminal 0 para informar que meu programa chegou até o final sem problemas de execução.
}