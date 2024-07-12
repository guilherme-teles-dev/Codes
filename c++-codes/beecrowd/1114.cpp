/*
Autor: Guilherme B. Teles
Descrição: Programa validador de senha.
Entrada: Uma tentativa de senha
Saída: "Senha Invalida" caso a senha não for correta ou "Acesso Permitido" caso a senha digitada seja a correta.
*/
#include <iostream> //Inclusão da biblioteca responsável por permitir a entrada e saída de dados através do cin e cout.
using namespace std; //Parâmetro para encurtar o uso de comandos para melhorar a legibilidade e escrita do código.

//Código principal
int main(){
    int senha = 2002; //Crio uma variável que comportará a senha.
    bool acesso_negado = true; //Crio uma variável para monitorar se a senha foi ou não acertada.
    
    //Crio um looping.
    while(acesso_negado){ //Esse looping funcionará até a senha ser acertada.
        int tentativa; //Crio uma variável do tipo inteira para receber a tentativa da vez.
        cin >> tentativa; //Coloco uma tentativa nova na variável tentantiva.
        
        //Crio uma condicional para verificar a corretude da tentativa.
        if(tentativa != senha){ //Em caso da tentativa ter sido diferente da senha
            cout << "Senha Invalida" << endl; //Informo que a senha é invalida.
        }
        else{ //Em caso delas coincidirem
            cout << "Acesso Permitido" << endl; //Informo que a senha digitada é correta
            acesso_negado = false;//Troco o estado da variável de monitoramento de looping para falso, o que fará com que o looping não se repita mais uma vez.
        }
    }
    
    return 0; //Informo para o terminal que o programa chegou até o final sem erros de execução.
}
