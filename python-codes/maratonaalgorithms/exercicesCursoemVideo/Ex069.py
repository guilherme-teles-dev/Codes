pessoas_mais_18 = 0
homens = 0
mulheres_menos_20 = 0
while True:
    idade = str(input('Digite sua idade: '))
    while idade.isnumeric() == False:
        idade = str(input('Idade invalida, Digite novamente: '))
    idade = int(idade)
    sexo = str(input('Digite o seu sexo: (M/F) ')).upper()
    while sexo not in 'FM' or sexo == '':
        sexo = str(input('Sexo invalido, digite novamente: '))
    if idade < 20 and sexo == 'F':
        mulheres_menos_20 += 1
    elif sexo == 'M':
        homens += 1
    if idade > 18:
        pessoas_mais_18 += 1
    r = str(input('Deseja continuar? (S/N) ')).upper()
    while r not in 'SN':
        r = str(input('Resposta invalida, insira uma respota valida: (S/N) '))
    if r == 'N':
        break
print(f'''Foram cadastradas {pessoas_mais_18} pessoas com mais de 18 anos.
Foram cadastrados {homens} homens.
Foram cadastrados {mulheres_menos_20} mulheres com menos de 20 anos. ''')
