algoritmo "semnome"
var
   soma, divisao5, nulos, somap, c, numero: inteiro
   media: real
inicio
      c <- 1
      soma <- 0
      divisao5 <- 0
      nulos <- 0
      somap <- 0
      media <- 0
      repita
            escreva("Digite o ", c,"° termo: ")
            leia(numero)
            se (numero % 2 = 0) entao
               somap <- somap + numero
            FimSe
            se (numero = 0) entao
               nulos <- nulos + 1
            Fimse
            media <- media + (numero/2)
            se (numero % 5 = 0) entao
               divisao5 <- divisao5 + 1
            Fimse
            soma <- soma + numero
            c <- c+1
      ate(c > 5)
      escreval("A soma entre os valores é ", soma)
      escreval("A media entre os valores é ", media)
      escreval("A quantidade de multiplos de 5 é ", divisao5)
      escreval("A quantidade de numeros nulos são ", nulos)
      escreval("A soma dos valores pares é ", somap)
fimalgoritmo
