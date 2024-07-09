pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = 2021-(int(input('Ano de nascimento: ')))
pessoa['carteira de trabalho'] = int(input('Carteira de trabalho: '))
if pessoa['carteira de trabalho'] != 0:
    pessoa['ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: '))
    pessoa['aposentadoria'] = pessoa['idade']+(35-(2021 - pessoa['ano de contratação']))
for c, v in pessoa.items():
    print(f'{c} tem o valor {v}')
