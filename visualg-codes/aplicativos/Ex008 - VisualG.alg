algoritmo "semnome"
var
   genero, resp: caractere
   idade, cor_cabelo, homemm18, mulherm25: inteiro
inicio
      mulherm25 <- 0
      homemm18 <- 0
      repita
            escreval("Qual é o Sexo? [M/F] ")
            leia(genero)
            escreval("Qual é a idade? ")
            leia(idade)
            escreval("Qual é a cor do cabelo? ")
            escreval("[1] - Preto ")
            escreval("[2] - Castanho ")
            escreval("[3] - Loiro ")
            escreval("[4] - Ruivo ")
            leia(cor_cabelo)
            escreval("Quer continuar? ")
            leia(resp)
            se (genero = "M") e (idade > 18) e (cor_cabelo = 2) entao
               homemm18 <- homemm18 + 1
            FimSE
            se (genero = "F") e (idade >= 25) e (idade <= 30) e (cor_cabelo = 3) entao
               mulherm25 <- mulherm25 + 1
            FimSE
      ate (resp = "N")
      escreva("Existem ", homemm18, " homens com mais de 18 anos e cabelos castanhos. ")
      Escreva("Existem ", mulherm25, " mulheres entre 25 e 30 anos e loiras. ")
fimalgoritmo
