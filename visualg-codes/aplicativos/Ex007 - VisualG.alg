algoritmo "semnome"
var
   cont, resp: inteiro
inicio
      repita
            escreval("Pressione -")
            escreval("[1] - Para contar de 1 a 10.")
            escreval("[2] - Para contar de 10 a 1.")
            escreval("[3] - Para sair.")
            leia(resp)
            se (resp = 1) entao
               cont <- 1
               enquanto (cont <= 10) faca
                        escreval(cont)
                        cont <- cont + 1
               FimEnquanto
            senao
                 Se(resp = 2) entao
                         cont <-10
                         enquanto (cont >= 0) faca
                                  escreval(cont)
                                  cont <- cont - 1
                         FimEnquanto
                 senao
                      se (resp = 3) entao
                         escreval("Até a proxima! ")
                      senao
                           escreval("Alternativa inexistente. ")
                      FimSe
                 FimSE
            FimSe
      ate(resp = 3)
fimalgoritmo
