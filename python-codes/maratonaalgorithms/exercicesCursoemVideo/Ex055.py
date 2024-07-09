maior_peso = 0
menor_peso = 0
for c in range (0, 5):
    peso = float(input('Digite o peso: '))
    if c == 0:
        maior_peso = peso
        menor_peso = peso
    else:
        if maior_peso < peso:
            maior_peso = peso
        elif menor_peso > peso:
            menor_peso = peso
print(f'O menor peso lido foi: {menor_peso}! ')
print(f'O maior peso lido foi: {maior_peso}! ')
