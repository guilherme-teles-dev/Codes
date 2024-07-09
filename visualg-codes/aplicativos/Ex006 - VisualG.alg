algoritmo "semnome"
var
   maior_nota, nota: real
   melhor_aluno, aluno: caractere
   alunos, contador: inteiro
inicio
      escreva("Quantos alunos tem na turma: ")
      leia(alunos)
      contador <- 1
      maior_nota <- 0
      melhor_aluno <- ""
      enquanto (contador <= alunos) faca
               escreva("Nome do aluno: ")
               leia(aluno)
               escreva("Nota do aluno: ")
               leia(nota)
               Se (maior_nota < nota) entao
                  maior_nota <- nota
                  melhor_aluno <- aluno
               FimSE
               contador <- contador + 1
      fimenquanto
      escreva("O melhor aluno foi ", melhor_aluno, " com a nota de ", maior_nota, "! ")
fimalgoritmo
