algoritmo "Voc� est� apto a dirigir? "
var
   ano_nascimento, ano_atual, idade: inteiro
inicio
      escreva("Ano de nascimento(yyyy): ")
      leia(ano_nascimento)
      escreva("Ano atual(yyyy): ")
      leia(ano_atual)
      idade <- ano_atual - ano_nascimento
      escreval("Voc� tem ", idade, " anos.")
      se (idade < 18) entao
         escreval("Voc� n�o est� apto a dirigir!")
      senao
           escreval("Voc� est� apto a dirigir! ")
      FimSe
fimalgoritmo
