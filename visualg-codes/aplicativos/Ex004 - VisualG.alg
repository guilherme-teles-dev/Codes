algoritmo "semnome"
var
   time1, time2, resultado: inteiro
inicio
      escreva("Quantos gols o primeiro time fez? ")
      leia(time1)
      escreva("Quantos gols o segundo time fez? ")
      leia(time2)
      resultado <- time1 - time2
      
      se (abs(resultado) < 5) e (abs(resultado) > 0) entao
         Escreva("Partida normal. ")
      senao
           se (abs(resultado) >= 5) entao
              escreva("Goleada. ")
           senao
                escreva("Empate. ")
           FimSe
      FimSe
fimalgoritmo
