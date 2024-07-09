algoritmo "semnome"
var
   i, f: inteiro
inicio
      escreva("Inicio: ")
      leia(i)
      escreva("Final: ")
      leia(f)
      se (i > f) entao
         enquanto (i >= f) faca
                  escreva(i)
                  i <- i -1
         FimEnquanto
      senao
           se (i = f) entao
              escreva(i)
           senao
                enquanto (i <= f) faca
                         escreva(i)
                         i <- i+1
                FimEnquanto
           FimSe
      FimSE
fimalgoritmo
