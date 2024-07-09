algoritmo "Você está apto a dirigir? "
var
   ano_nascimento, ano_atual, idade: inteiro
inicio
      escreva("Ano de nascimento(yyyy): ")
      leia(ano_nascimento)
      escreva("Ano atual(yyyy): ")
      leia(ano_atual)
      idade <- ano_atual - ano_nascimento
      escreval("Você tem ", idade, " anos.")
      se (idade < 18) entao
         escreval("Você não está apto a dirigir!")
      senao
           escreval("Você está apto a dirigir! ")
      FimSe
fimalgoritmo
