sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo: (M/F) ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Valor invalido! Tente novamente!')
if sexo == 'M':
    print('Seu sexo é masculino! ')
elif sexo == 'F':
    print('Seu sexo é feminino! ')
