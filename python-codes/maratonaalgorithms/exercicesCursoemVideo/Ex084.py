pesadas = []
leves = []
cadastros = 0
while True:
    pessoa = []
    pessoa.append(str(input('Digite o nome: ')))
    pessoa.append(float(input('Digite o peso: ')))
    cadastros += 1
    if pessoa[1] <= 70:
        leves.append(pessoa)
    elif pessoa[1] >= 100:
        pesadas.append(pessoa)
    r = str(input('Quer continuar? (S/N) '))
    if r in 'Nn':
        break
print(f'Foram cadastradas {cadastros} pessoas. ')
print(f'O maior peso foi de 100Kg. Peso de ', end='')
for c in pesadas:
    print(c[0], end='')
print()
print(f'O menor peso foi de 70Kg. Peso de ', end='')
for c in leves:
    print(c[0], end='')
print()
