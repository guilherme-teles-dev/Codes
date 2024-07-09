algoritmo "semnome"
var
   n1, n2, media: real
inicio
      escreva("Digite a primeira nota: ")
      leia(n1)
      escreva("Digite a segunda nota: ")
      leia(n2)
      media <- (n1+n2)/2
      escreval("A media desse aluno é de ", media)
      escreva("Aproveitamento do Aluno: ")

      se (media < 5) entao
         escreva("F")
      senao
           se (media >= 5) e (media < 6) entao
              escreva("E")
           senao
                se (media >= 6) e (media < 7) entao
                   escreva("D")
                senao
                     se (media >= 7) e (media < 8) entao
                        escreva("C")
                     senao
                          se (media >= 8) e (media < 9) entao
                             escreva("B")
                          senao
                               se (media >= 9) entao
                                  escreva("A")
                               FimSe
                          FimSe
                     FimSe
                FimSe
           FimSe
      Fimse
fimalgoritmo
