idade = int(input('Digite a idade do atleta: '))
if idade <= 9:
    print('Categoria Mirim. ')
elif idade > 9 and idade <= 14:
    print('Categoria Infantil. ')
elif idade > 14 and idade <= 19:
    print('Categoria Junior. ')
elif idade > 19 and idade <= 20:
    print('Categoria Sênior. ')
else:
    print('Categoria Master. ')
