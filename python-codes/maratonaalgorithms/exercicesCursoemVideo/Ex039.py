idade = int(input('Informe a idade do jovem: '))
if idade < 18:
    print(f'O jovem ainda não está na idade de se alistar! Faltam {18-idade} anos para o alistamento! ')
elif idade == 18:
    print('O jovem está na idade de se alistar! ')
else:
    print(f'O jovem já passou da idade de se alistar! Passou {idade-18} anos da idade do alistamento! ')
