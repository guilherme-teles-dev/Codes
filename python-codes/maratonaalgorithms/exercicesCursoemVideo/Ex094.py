pessoas = list()
while True:
    pessoa = dict()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa)
    r = str(input('Deseja continuar? (S/N) '))
    if r in 'Nn':
        break
print(f'- O grupo tem {len(pessoas)} pessoas. ')
media = 0

for c in range(0, len(pessoas)):
    media += (pessoas[c]['idade'])/len(pessoas)
print(f'- A média de idade é de {media} anos. ')
print(f'- As mulheres cadastradas foram ', end='')
for c in pessoas:
    if c['sexo'] == 'F':
        print(f'{c["nome"]} ', end='')
print()
print('- Lista das pessoas que estão acima da média: ')
for c in pessoas:
    if c['idade'] > media:
        print(c)
print('<< Encerrado >>')
