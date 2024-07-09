aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
if aluno['media'] < 7:
    aluno['situação'] = 'Reprovado'
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
print(f'Situação é igual a {aluno["situação"]}')
